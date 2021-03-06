import urllib2, re, pytz

from datetime import datetime, date
from lxml import etree
from StringIO import StringIO

from dateutil.parser import parse as dateparse


est=pytz.timezone('US/Eastern')

USER_AGENT = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.0.4) Gecko/2008102920 Firefox/3.0.4"

rss_url = "https://stations.fcc.gov/rss/"

tempfile = "scraper/rss.xml"

url_re = re.compile('Click\s*<a href="(.*?)">here</a>\s*to open the report')
political_re = re.compile('Political\s+File', re.I)
datetime_re = re.compile('uploaded <b>(.*?)</b> in <b><a href="(.*?)">(.*?)</a></b> on ([\d\/]+) (\d+\:\d+) ([ap]m)')
file_url_re = re.compile(r'collect/files/(\d+)/Political File/(.+)')
file_domain = "https://stations.fcc.gov/"



def parse_file_url(url):
    url_parts = re.findall(file_url_re, url)
    (fac_id, pathArray) = (None, None)
    if url_parts:
        fac_id = url_parts[0][0]
        path = url_parts[0][1]
        pathArray = path.split('/')
    else: 
        print "Couldn't parse file path %s" % (url)
        
    return fac_id, pathArray
    
def parse_xml_from_text(xml):
    datefound = date.today()
    political_files = []
    tree = etree.parse(StringIO(xml))
    results = []
    
    for  elt in tree.getiterator('{http://www.w3.org/2005/Atom}feed'):
        for childelt in elt.getiterator('{http://www.w3.org/2005/Atom}entry'):
            stringtext =  etree.tostring(childelt, pretty_print=True)
            [date_found, timefound] = [None, None]
            [title, full_folder_path, folder_path, date_loaded, time_loaded, time_pm] = [None, None, None, None, None, None] 
            datafound = re.search(datetime_re, stringtext)
            if datafound:
                (title, full_folder_path, folder_path, date_loaded, time_loaded, time_pm) = datafound.groups()
                date_found = dateparse(date_loaded)
                time_found = datetime.strptime(date_loaded + " " + time_loaded + " " + time_pm, '%m/%d/%Y %I:%M %p')
            else:
                pass
                #print "!! no path / date info found"
                
            
            urlfound = re.search(url_re, stringtext)
            [federal_office, federal_district, office, district] = [None, None, None, None]
            is_outside_group = False
            if urlfound:
                this_url = urlfound.group(1)
                if re.search(political_re, this_url):
                    #print "Found political file url: %s \n\n" % (this_url)
                    
                    (facility_id, details) = parse_file_url(this_url)
                    
                    if (details[1] == 'Non-Candidate Issue Ads'):
                        is_outside_group = True 
                    elif (details[1] == 'Federal'):
                        office = details[2]
                        if (office == 'US House'):
                            district = details[3]
                    # They're not very consisten about this... 
                    path = details[1:]
                    name = path[-2:-1][0]

                    # hard truncate. This data's a mess.
                    ad_type =details[1]
                    if office:
                        federal_office = office[:31]
                    if district:
                        federal_district = district[:31]
                    raw_name_guess = name[:255]
                    
                    
                    filestub = {
                        'title':title,
                        'full_folder_path':full_folder_path,
                        'date_loaded':date_found,
                        'time_loaded':time_found,
                        'href':file_domain + this_url,
                        'facility_id':facility_id,
                        'year':details[0],
                        'ad_type':ad_type,
                        'federal_office':federal_office,
                        'federal_district':federal_district,
                        'raw_name_guess':raw_name_guess,
                        'is_outside_group':is_outside_group
                    }
                    political_files.append(filestub)
                    
                else:
                    pass
                    #print "Other file url %s\n\n" %  (this_url)
            else:
                # It seems that files that don't have this link haven't finished processing. Ignore them, with unknown consequences.
                print "URL missing!! "
                
    return political_files
                

def get_rss_from_web():
    headers = {'User-Agent': USER_AGENT}   
    data = None       
    req = urllib2.Request(rss_url, data, headers)
    response = urllib2.urlopen(req)
    rssdata = response.read()
    return rssdata


def write_rss_to_file(rssdata):
    outfile = open(tempfile, 'w')
    outfile.write(rssdata)
    outfile.close()

def get_rss_from_file():
    infile = open(tempfile, 'r')
    return infile.read()

if __name__ == '__main__':
    rssdata = get_rss_from_file()
    political_files = parse_xml_from_text(rssdata)
    for f in political_files:
        print f
