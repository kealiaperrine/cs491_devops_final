FROM python:3

ADD sources/follow.py /

ADD sources/main.py / 

ADD sources/monster.py / 

ADD sources/physics.py /

ADD sources/player.py /

CMD ["python", "./main.py"]
