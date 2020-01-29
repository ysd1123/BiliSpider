import get_video
import get_user


for i in range(20):
    if get_video.data(i+1) != 'Video 404':
        print(get_video.data(i+1)['view'])
for j in range(20):
    if get_user.data(j+1) != 'User 404':
        print(get_user.data(j+1)['follower'])