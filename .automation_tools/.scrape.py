# STAFF

# from bs4 import BeautifulSoup
# import requests

# url = 'https://mcf.knust.edu.gh/index.php/staff'

# res = requests.get(url)
# print(res.status_code)

# soup = BeautifulSoup(res.content, 'html.parser')

# res = soup.find_all("div", class_="col-sm-2")

# lect_imgs = ["https://mcf.knust.edu.gh"+i.find("img").get('src') for i in res]
# lect_name = [i.find("img").get('title') for i in res]
# lect_role = [i.find("h5").text.strip() for i in res]

# res = zip(lect_imgs, lect_name, lect_role)

# new = ["""
#         <div class="item">
#                     <div class="single-team-inner">
#                         <div class="thumb">
#                             <img src="{}" alt="img">
#                         </div>
#                         <div class="details">
#                             <h4><a href="#">{}</a></h4>
#                             <span>{}</span>
#                         </div>
#                     </div>
#                 </div>
#         """.format(_[0], _[1], _[2]).replace("\n", "") for _ in list(res)]


# with open("dump.txt", 'w') as f:
#     f.write(''.join(new))

# ===============================================================================================================================
# ===============================================================================================================================
# ===============================================================================================================================

# COHORT

from bs4 import BeautifulSoup
import requests

url = 'https://mcf.knust.edu.gh/index.php/scholars/cohort-two'

res = requests.get(url)
print(res.status_code)

soup = BeautifulSoup(res.content, 'html.parser')

res = soup.find_all("div", class_="featured-image")

lect_imgs = ["https://mcf.knust.edu.gh"+i.find("img").get('src') for i in res]

res = soup.find_all("div", class_="profile-name")

lect_role = [i.find("h5").text.strip() for i in res]
lect_name = [i.find("h4").text.strip() for i in res]

res = zip(lect_name, lect_role)

x= [' '.join(i[0].replace("\t", "").split()) for i in list(res)]

print(len(x))


# new = ["""
#         <div class="col-lg-4 col-md-6">
#                     <div class="single-team-inner">
#                         <div class="thumb">
#                             <img src="{}" alt="img">
#                         </div>
#                         <div class="details">
#                             <h4><a href="#">{}</a></h4>
#                             <span>{}</span>
#                         </div>
#                     </div>
#                 </div>
#         """.format(_[0], _[1], _[2]).replace("\n", "") for _ in list(res)]


# with open("dump.txt", 'w') as f:
#     f.write(''.join(new))

# ===============================================================================================================================
# ===============================================================================================================================
# ===============================================================================================================================
