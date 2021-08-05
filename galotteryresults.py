import json
import re
from datetime import date
from time import sleep

import ga_api_endpoints
import requests
from bs4 import BeautifulSoup, SoupStrainer

day_dict = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun",
    7: "Jul",
    8: "Aug",
    9: "Sep",
    10: "Oct",
    11: "Nov",
    12: "Dec",
}


def get_info(url="athensga.craigslist.org"):
    job_url = f"{url}/search/jjj?query=voice+over+%7C+voice+jobs+%7C+voice+wanted+%7C++voiceovers+%7C+voice+talent+%7C+voice+recordings"
    gig_url = f"{url}/search/ggg?query=voice+over+%7C+voice+jobs+%7C+voice+wanted+%7C++voiceovers+%7C+voice+talent+%7C+voice+recordings"
    payload = {}
    headers = {
        'Cookie': 'cl_b=4|93fc8594e7b76f0c01a65a2c12434158c5a57e95|1625772264ONi0U'}
    job_response = requests.request("GET", job_url)
    gig_response = requests.request("GET", gig_url)
    results = {"jobs": job_response, "gig": gig_response}
    return results
    '''
    get all elements for <ul class="rows" id="search-results">
    iterate each list <li class="result-row" data-pid="7349349885">
    if date equals to current date, then add URL (, a href) to list
        <time class="result-date" datetime="2021-07-11 05:11" title="Sun 11 Jul 05:11:36 AM">Jul 11</time>
        <a href="https://losangeles.craigslist.org/sfv/tlg/d/van-nuys-auditions-actor-singers-for/7349349885.html" class="result-image gallery empty"></a>

   
    '''


def get_list_of_us_cities():
    results = requests.request("GET", "https://geo.craigslist.org/iso/us")
    site = "geo-site-list-container"
    soup = BeautifulSoup(results.content, parse_only=SoupStrainer('a'))
    sitelinks = []
    craigslist_regex = "https:\/\/\w+\.craigslist\.org"
    for link in soup:
        if link.has_attr('href') and re.match(craigslist_regex, link['href']) and not re.match("https:\/\/(www|forums)\.craigslist\.org", link['href']):
            sitelinks.append(link['href'])
    return sitelinks


def get_search_results(response):
    response = requests.request(
        "GET", "https://atlanta.craigslist.org/search/jjj?query=office")
    soup = BeautifulSoup(response.content, 'html.parser')
    search_results = soup.find(id="search-results")
    list_results = search_results.find_all(search_results, class_="result-row")
    list_results[1].find("time").string
    today = date.today()
    today_craigslist = f"{day_dict[today.month]} {today.day}"
    final_results = []
    for result in list_results:
        if result.find("time").string == today_craigslist:
            final_results.append(result)
    # need to parse out the rest of the info and insert as key/value pairs, then append to final_results
    '''
    <li class="result-row" data-pid="7350278589" data-repost-of="7321752389">
    <a class="result-image gallery" data-ids="3:00808_aymhwYCrVkJz_0wg0ka" href="https://atlanta.craigslist.org/atl/ofc/d/decatur-administrative-assistant/7350278589.html">
    </a>
    <div class="result-info">
    <span class="icon icon-star" role="button">
    <span class="screen-reader-text">favorite this post</span>
    </span>
    <time class="result-date" datetime="2021-07-13 07:10" title="Tue 13 Jul 07:10:14 AM">Jul 13</time>
    <h3 class="result-heading">
    <a class="result-title hdrlnk" data-id="7350278589" href="https://atlanta.craigslist.org/atl/ofc/d/decatur-administrative-assistant/7350278589.html" id="postid_7350278589">Administrative Assistant</a>
    </h3>
    <span class="result-meta">
    <span class="result-hood"> (Decatur)</span>
    <span class="result-tags">
    <span class="pictag">pic</span>
    </span>
    <span class="banish icon icon-trash" role="button">
    <span class="screen-reader-text">hide this posting</span>
    </span>
    <span aria-hidden="true" class="unbanish icon icon-trash red" role="button"></span>
    <a class="restore-link" href="#">
    <span class="restore-narrow-text">restore</span>
    <span class="restore-wide-text">restore this posting</span>
    </a>
    </span>
    </div>
    </li>
    '''
    pass


def jdump(obj):
    print(json.dumps(obj, indent=2))


response = get_info("https://athensga.craigslist.org")


'''
Here's the plan:
first  - figure out what the url is to search for each jobs listing

if no results, pass
no results: 

<div class="content" id="sortable-results">
                <section class="favlistsection">
                    <section class="favlistinfo">
                    </section>
                    <section class="banishlistinfo">
                    </section>
                </section>


                    

                    <div class="alert alert-sm alert-warning">Nothing found for that search. (All words must match.)
</div>

second - figure out how to format the return data
third - get list of all cities
fourth - iterate through all cities to search 
fifth - display results? email?


'''
