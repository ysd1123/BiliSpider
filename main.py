import get_video
import get_user
import get_up


for i in range(20):
    if get_video.data(i+1) != 'Video 404':
        print(i+1, get_video.data(i+1)['view'])
print('------------------------------')
for j in range(20):
    if get_user.data(j+1) != 'User 404':
        print(j+1, get_user.data(j+1)['follower'])
print('------------------------------')
for k in range(20):
    if get_up.data(k+1) != 'Up 404':
        print(k+1, get_up.data(k+1)['likes'])
