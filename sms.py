a

    \ | �_�   �                   

@

   s�   d dl mZ d dlZd dlZd dlZdZdZdZdZdZ
dZ
d
Zd
Z
dd � Z
d
d� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Ze�  dS )�    ��postNz[0mz[31mz[1;
32
mz[33mz[34mz[35mz[36mz[37
                                 mc                   C   s8   t �d� t �d� td� td� td� td� d S )N�clearztoilet - f
mono12 - F
gay
"SMS"� z
'[1;32m       -----SPAM SMS (Unlimited sms for free)-----z[31m)�os�system�print� r	   r	   �sms.py�banner   s    

r   c                 C   s   d} |  dd�}t  |  | d�}d S )Nz
'https://guru.lk/auth/headstart/ajax.phpZsms_reg)Zphone�action)�datar   )�number�delayZurlr
   Zpossr       r       r
   �gurulk   s    
r   c                   C   s
   t �  d S )N)�askr       r       r       r
   �back  #    s    r   c                   C   sF   t �  t�d� t�d� t�d� t�d� t�d� t�d� d S )NZcdz
rm - rf
SMSz(git
clone
https: // github.com / mastersl26 / smszcd
smszpip
install - r
requirements.txtz
python
sms.py)r   r   r   r       r       r       r
   �update &   s    




r   c                  C   sr   t �  td� td� td� td� td� td�}  |  dkrDt�   |  dkrRt�   |  dkr
`t�   |  dkrnt�  d S )    Nr   z[1;
32
m1.Set
Count
z[35m2.unlimited z
[1;
32
m3.Backz[33mEnter your choice: �1�2�3)r   r   �input�sms�    unlimitedr   �choice)Zinppr       r       r
   r    /    s    r   c                 C   s4   t  | �}t  |  �}td |  d  |  d d d � d S )Nz sending
OTP... �    z Sent
Successfully �
)�strr   )�countr   ZnumZcounr       r       r
   �sentB   s    r   c                  C   s\   t �  td� td�} td�}td�}d}t | �} |  | k rXt |   | �  | d7 }t |  |  � q2d S )Nr   �[
    35mEnter the number: z[34mEnter the count: z[1;
32
mEnter
the
delay
time: r   �   )r   r   r   �intr   r   )r   �timesr   �i�timer       r       r
   r   G   s    
r   c                  C   sD   t �  td� td�} td�}d}t |   | �  | d7 }t |  |  � q
"d S )Nr   r    z[36mEnter the delay time : r   r!   )r   r   r   r   r   )r   r   r$   r	   r	   r
   r   V   s    
r   c                  C   sr   t �d� t�  td� td� td� td� td� td� td� td� td� td�}  |  dkrnt�  d S )    Nr   r   z,[
    1;
32
m1.Support
for only Sri Lankan Numbers.
z6[36mSupport me >> Github - https://
    github.com / mastersl26zJ[34m >> Youtube - MASTER SL z * If you know more web site Apis.send me.z![1;
32
mPress
Enter
To
Continue: )r   r   r   r   r   r   �Zinpr       r       r
   �aboutb   s    
r'   c                  C   s�   t �  td� td� td� td� td� td� td� td�} | dkrTt�  | dkrbt�  | d	krpt�  | d
kr�td� td� td � t�   |  dkr�t�  d S )
Nr   z[34m1.Start Toolz[35m2.Update Toolz[1;
32
m3.Aboutz[33m4.Exitz[36mEnter Your Option >> > r   r   r   �4
z[35mThank You zCODED
BY
MASTER SL)r   r   r   r   r   r'   �exitr   r&   r	   r	   r
   r   r   s,    r   )Zrequestsr   r   r %   �sys�W�R�G�O�B�P�CZGRr   r   r   r   r   r   r   r   r'   r   r	   r	   r	   r
   � < module >   s,         
