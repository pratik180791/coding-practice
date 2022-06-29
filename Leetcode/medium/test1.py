"""

/*
Enter your query here.
*/

select * from orders where status!='DELIVERED' order by order_date, id limit 5;
"""
import requests
import logging
def  getTopicCount(topic):
    base_url = f"https://en.wikipedia.org/w/api.php?action=" \
               f"parse&section=0&prop=text&format=json&page={topic}"
    if not topic:
        return
    url = base_url.format(topic)
    print(url)
    resp = requests.get(url)
    if not resp.ok:
        logging.info(f"Invalid response received for url {url}")
        return -1
    article_text = resp.json()

    print(article_text.keys())
    cnt = 0
    for key, val in article_text["parse"]["text"].items():
        cnt += val.lower().count(topic.lower())
    return cnt


#op = getTopicCount("water")
#print(op)

products = ["yellowShirt","redShirt",
            "blackPants", "redShirt",
            "greenPants", "blackPants","yellowShirt"]

products = ["redShirt", "greenPants", "redShirt", "orangeShoes", "blackPants", "blackPants"]
res = {}
for prod in products:
    if prod in res:
        res[prod] += 1
    else:
        res[prod] = 1

print(res)
res = sorted(res)
print(res)
print(res[-1])
#sorted(student_tuples, key=lambda student: student[2])

print(sorted(tasks, reverse=True))
