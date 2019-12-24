"""
С помощью паттерна "Наблюдатель" реализуйте простую систему подписок и уведомлений видеохостинга MyTube.

Для реализации можно использовать следующие определения классов:

MyTubeChannel - канал, у которого есть владелец.
    Параметры:
        name: str - Название канала
        owner: MyTubeUser - Владелец канала
        playlists: Dict[str, List[str]] - Плейлисты на канале ({'Название плейлиста': ['видео 1', 'видео 2', 'видео 3']})

    Методы:
        __init__(channel_name: str, chanel_owner: MyTubeUser) - При создании канала указывается название канала и его владелец
        subscribe(user: MyTubeUser) - Подписка пользователя user на канал
        publish_video(video: str) - Публикация нового видео и рассылка новости о публикации всем подписчикам
        publish_playlist(name: str, playlist: List[str]) - Публикация нового плейлиста и рассылка новости о публикации всем подписчикам

MyTubeUser - Пользователь видеохостинга MyTube
    Параметры:
        _name: str - Имя пользователя MyTube
    Методы:
        __init__(user_name: str) - У нового пользователя есть имя
        update(message: str): - Метод для приёма уведомлений о публикации

Пример кода, который должен работать:

matt = MyTubeUser('Matt')
john = MyTubeUser('John')
erica = MyTubeUser('Erica')

dogs_life = YoutubeChannel('All about dogs', matt)
dogs_life.subscribe(john)
dogs_life.subscribe(erica)

dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos]

for video in dogs_nutrition_videos:
    dogs_life.publish_video(video)

dogs_life.publish_playlist(dogs_nutrition_playlist)

Output:
Dear John, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear Erica, there is new video on 'All about dogs' channel: 'What do dogs eat?'
Dear John, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear Erica, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
Dear John, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'
Dear Erica, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'

"""
class MyTubeUser:
    def __init__(self, user_name: str):
        self._name = user_name
        
    def update(self, message: str):
        print(message)

        
class MyTubeChannel:
    playlists = {}
    
    def __init__(self, channel_name: str, channel_owner: MyTubeUser):
        self.name = channel_name
        self.owner = channel_owner
        self._subscribers = set()

    def subscribe(self, user: MyTubeUser):
        self._subscribers.add(user)
        
    def publish_video(self, video: str):
        for subscriber in self._subscribers:
            subscriber.update(f"Dear {subscriber._name}, there is new video on '{self.name}' channel: '{video}'")
        
    def publish_playlist(self, name: str, playlist: list):
        for subscriber in self._subscribers:
            subscriber.update(f"Dear {subscriber._name}, there is new playlist on '{self.name}' channel: '{name}'")
        
                            
matt = MyTubeUser('Matt')
john = MyTubeUser('John')
erica = MyTubeUser('Erica')

dogs_life = MyTubeChannel('All about dogs', matt)
dogs_life.subscribe(john)
dogs_life.subscribe(erica)

dogs_nutrition_videos = ['What do dogs eat?', 'Which Pedigree pack to choose?']
dogs_nutrition_playlist = {'Dogs nutrition': dogs_nutrition_videos}
for video in dogs_nutrition_videos:
    dogs_life.publish_video(video)
dogs_life.publish_playlist('Dogs nutrition', dogs_nutrition_playlist)

#Output:
#Dear John, there is new video on 'All about dogs' channel: 'What do dogs eat?'
#Dear Erica, there is new video on 'All about dogs' channel: 'What do dogs eat?'
#Dear John, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
#Dear Erica, there is new video on 'All about dogs' channel: 'Which Pedigree pack to choose?'
#Dear John, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'
#Dear Erica, there is new playlist on 'All about dogs' channel: 'Dogs nutrition'

