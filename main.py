from fastapi import FastAPI
import instaloader
import uvicorn
from utility import mycollection, credentilas_collection
from models import login_model

app = FastAPI()

@app.post('/login')
def login(logindetail:login_model):
    credentilas_collection
    L = instaloader.Instaloader()
    L.login(logindetail.username, logindetail.password)

    new_followers_list = []
    profile = instaloader.Profile.from_username(L.context, logindetail.username)
    for follower in profile.get_followers():
        new_followers_list.append(follower.username)
        followerdetail = {
            "username": follower.username,
            "full_name": follower.full_name,
            "profile_pic_url": follower.profile_pic_url,
            "mediacount": follower.mediacount,
            "biography": follower.biography,
            "followers": follower.followers,
            "followees": follower.followees,
            "is_private": follower.is_private,
            "is_verified": follower.is_verified,
        }
    
    old_followers = mycollection.find_one({'username':profile.username},{'_id': 0})
    old_followers_list = old_followers['followers_list']
    unfollowed_followers = [item for item in new_followers_list if item not in old_followers_list]


    mycollection.update_one({'username':profile.username}, {'$set': {'followers_list': new_followers_list}})

    return_data = {'Unfollowed_users':unfollowed_followers,
                   'all_followers':new_followers_list}
    return return_data



L = instaloader.Instaloader()
L.login("krishna_shanka", "8660572291")
profile = instaloader.Profile.from_username(L.context, "krishna_shanka")
for follower in profile.get_followers():
    print(follower.username)


if __name__ =='__main__':
    uvicorn.run(app, host = '0.0.0.0', port = 8000)