import requests
from bs4 import BeautifulSoup

def get_soup():
    r = requests.get("https://itexamanswers.net/ccna-3-v7-0-final-exam-answers-full-enterprise-networking-security-and-automation.html")

    soup = BeautifulSoup(r.content, 'html.parser')

    return soup

def get_answers(soup: BeautifulSoup, question):
    element = soup.find('strong', string=lambda text: question in text if text else False)
    
    if element == None:
        return []
    
    next_strong = element.find_next('strong')
    answers = []

    if next_strong.text.partition('. ')[0].isnumeric():
        for tag in element.next_elements:
            if tag == next_strong:
                break
            elif tag.name == 'p':
                answers.append(tag.text)
        return answers
    
    while not next_strong.text.partition('. ')[0].isnumeric() and next_strong != None and next_strong.text != 'Explanation:':
        answers.append(next_strong.text)
        next_strong = next_strong.find_next('strong')
        
    return answers

if __name__ == "__main__":
    soup = get_soup()
    a = get_answers(soup, "27. Refer to the exhibit. The network administrator that has the IP address of 10.0.70.23/25 needs to have access to the corporate FTP server (10.0.54.5/28). The FTP server is also a web server that is accessible to all internal employees on networks within the 10.x.x.x address. No other traffic should be allowed to this server. Which extended ACL would be used to filter this traffic, and how would this ACL be applied? (Choose two.)")
    print(a)