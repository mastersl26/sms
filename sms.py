a
    \|ฒ_฿  ใ                   @   s   d dl mZ d dlZd dlZd dlZdZdZdZdZdZ	dZ
d	Zd
Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Zdd Ze  dS )้    ฉฺpostNz[0mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37mc                   C   s8   t  dก t  dก td td td td d S )Nฺclearztoilet -f mono12 -F gay "SMS"ฺ z'[1;32m       -----SPAM SMS SENDER-----z[31m#CODED BY ISURUWA)ฺosฺsystemฺprintฉ r	   r	   ๚sms.pyฺbanner   s    

r   c                 C   s   d}| dd}t ||d}d S )Nz'https://guru.lk/auth/headstart/ajax.phpZsms_reg)Zphoneฺaction)ฺdatar   )ฺnumberฺdelayZurlr   Zpossr	   r	   r
   ฺgurulk   s    
r   c                   C   s
   t   d S )N)ฺaskr	   r	   r	   r
   ฺback#   s    r   c                   C   sF   t   t dก t dก t dก t dก t dก t dก d S )NZcdz
rm -rf SMSz(git clone https://github.com/isuruwa/SMSzcd SMSzpip install -r requirements.txtzpython sms.py)r   r   r   r	   r	   r	   r
   ฺupdate&   s    




r   c                  C   sr   t   td td td td td td} | dkrDt  | dkrRt  | dkr`t  | dkrnt  d S )	Nr   z[1;32m1.Set Count z[35m2.unlimited z[1;32m3.Backz[33mEnter your choice : ฺ1ฺ2ฺ3)r   r   ฺinputฺsmsฺ	unlimitedr   ฺchoice)Zinppr	   r	   r
   r   /   s    r   c                 C   s4   t |}t | }td| d | d d d  d S )Nz sending OTP ... ๚	z Sent Successfully ฺ
)ฺstrr   )ฺcountr   ZnumZcounr	   r	   r
   ฺsentB   s    r   c                  C   s\   t   td td} td}td}d}t|}||k rXt| | |d7 }t||  q2d S )Nr   ๚[35mEnter the number : z[34mEnter the count :z[1;32mEnter the delay time : r   ้   )r   r   r   ฺintr   r   )r   ฺtimesr   ฺiฺtimer	   r	   r
   r   G   s    
r   c                  C   sD   t   td td} td}d}t| | |d7 }t||  q"d S )Nr   r    z[36mEnter the delay time : r   r!   )r   r   r   r   r   )r   r   r$   r	   r	   r
   r   V   s    
r   c                  C   sr   t  dก t  td td td td td td td td td td} | dkrnt  d S )	Nr   r   z,[1;32m1.Support for only Sri Lankan Numberszd[34m2.Still contains only one website Api. More website Apis will be released with future updates.
z6[36mSupport me >> Github - https://github.com/isuruwazJ[34m          >>Facebook - https://www.facebook.com/isuru.umayanga.37819 z*If you know more web site Apis . send me .z![1;32mPress Enter To Continue : )r   r   r   r   r   r   ฉZinpr	   r	   r
   ฺaboutb   s    
r'   c                  C   sจ   t   td td td td td td td td} | dkrTt  | dkrbt  | d	krpt  | d
krtd td td t  | dkrคt  d S )Nr   z[34m1.Start Toolz[35m2.Update Toolz[1;32m3.Aboutz[33m4.Exitz[36mEnter Your Option  >>> r   r   r   ฺ4z[35mThank You zCODED BY ISURUWA)r   r   r   r   r   r'   ฺexitr   r&   r	   r	   r
   r   r   s,    r   )Zrequestsr   r   r%   ฺsysฺWฺRฺGฺOฺBฺPฺCZGRr   r   r   r   r   r   r   r   r'   r   r	   r	   r	   r
   ฺ<module>   s,   	