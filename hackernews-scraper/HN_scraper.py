from bs4 import BeautifulSoup
import requests
import pandas as pd




def fetch_pages(start_url):
    post_ranks = []
    post_titles = []
    storylinks = []
    scores = []
    post_authors = []
    post_age = []
    hn_data = {}

    while True:
        page = requests.get(start_url)
        print(start_url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text, 'lxml')

            ranks = soup.find_all('span', class_='rank')
            for rank in ranks:
                if rank:
                    post_ranks.append(rank.text)
                else:
                    post_ranks.append('')

            titles_and_links = soup.find_all('a', class_="storylink")
            for title in titles_and_links:
                if title:
                    post_titles.append(title.text)
                else:
                    post_titles.append('')

            for links in titles_and_links:
                if links:
                    storylinks.append(links["href"])
                else:
                    storylinks.append('')

            meta_data = soup.find_all('td', class_='subtext')
         
            for data in meta_data:
                score = data.find('span', class_="score")
                if score:
                    scores.append(score.text)
                else:
                    scores.append('')
                
                hnuser = data.find('a', class_='hnuser')
                if hnuser:
                    post_authors.append(hnuser.text)
                else:
                    post_authors.append('')

                age = data.find('span', class_='age')
                if age:
                    post_age.append(age.text)
                else:
                    post_age.append('')


            next_page = soup.find('a', class_='morelink')
            if next_page:
                next_page_url = "https://news.ycombinator.com/" + next_page["href"]
                start_url = next_page_url
            else:
                break
        else:
            print("Unable to access more pages", page.status_code)
            break
    
    hn_data["post_rank"] = post_ranks
    hn_data["author"] = post_authors
    hn_data["age"] = post_age
    hn_data["score"] = scores
    hn_data["post_link"] = storylinks
    hn_data["title"] = post_titles
    
    return hn_data


def create_dataframe_and_write_to_file(scrapped_data):
    hackernews_data = pd.DataFrame(scrapped_data)
    hackernews_data.to_csv("hackernews.csv")


if __name__ == "__main__":
    start_url = "https://news.ycombinator.com/"
    scrapped_data = fetch_pages(start_url)
    create_dataframe_and_write_to_file(scrapped_data)