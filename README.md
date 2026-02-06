## วิธีการ Hack เงินจากผู้ให้บริการ NFC Bolt Card
---
วิธีการ Hack Bolt Card ก็ไม่มีอะไรยาก นั่นก็คือการใช้ API ที่ LNBits มีให้นั่นแหละ<br>
<img width="1920" height="590" alt="2  LNbits API Document" src="https://github.com/user-attachments/assets/ea4e2915-b383-4e2f-8e5a-033fa378dd57" />
<br>
<img width="1446" height="818" alt="3  Bolt Card API Document" src="https://github.com/user-attachments/assets/d68c7bcd-6105-4143-b3ec-3770a6dd3e1a" />
<br>
<br>
<br>
1.หาวิธีให้ได้มาซึ่ง Invoice/Read Key และ Lightning Node URL ของ Account LNbits ที่ Bolt Card นั้นลงทะเบียนอยู่<br>
<img width="1221" height="709" alt="1  How toget Invoice read key" src="https://github.com/user-attachments/assets/a06e22b1-bb2f-488c-a23c-aa1872ed8fd2" />
<br>
<br>
<br>
2.จากนั้นทำการยิง API ไปหา Node ด้วยคำสั่งนี้ /boltcards/api/v1/cards<br>
[ขั้นตอนนี้คุณสามารถใช้ Code python ที่มีชื่อว่า Get_Data.py ในการดูดข้อมูลได้เลย]<br>
<img width="1412" height="692" alt="4  Get Bolt Card Data" src="https://github.com/user-attachments/assets/eb27e358-ffb7-4c40-a420-39532ec73b90" />
<br>
<br>
<br>
3.คุณจะได้มาซึ่งข้อมูลที่จำเป็นในการดูดเงินออกจาก Bolt Card นั่นก็คือ<br>
- UID<br>
- Counter Number<br>
- External ID<br>
- K1<br>
- K2<br>
<br>
<br>
<br>
4.จากนั้นให้คุณเอาข้อมูลที่ได้มาไปคำนวณหา SUN และ CMAC แล้วก็เอาทั้ง 2 ค่าไปประกอบเป็น lnurlw<br>
[ขั้นตอนนี้คุณสามารถใช้ Code python ที่มีชื่อว่า Cal_CMAC_SUN.py ในการสร้าง LNURLw ได้เลย]<br>
<img width="1411" height="693" alt="545379404-1dde2cdb-e83b-4809-8789-6fb1d962b339" src="https://github.com/user-attachments/assets/e643fc87-6061-4d8b-847f-1f00f6ddf362" />
<br>
<br>
<br>
5.เมื่อคุณได้ LNURLw มาแล้ว ก็ให้เอาไป Browse ที่ Google Chrome<br>
<img width="778" height="678" alt="545379639-e4915bbb-a966-44f8-a2e3-6ca8adc783a4" src="https://github.com/user-attachments/assets/3816bcc4-0115-4eaa-9199-ad5532fa38f6" />
<br>
<br>
<br>
6.จากนั้นให้คุณทำการ Copy ในส่วนของ Callback และค่า k1 ที่ถูก Generate มาจาก LNbits แล้วเก็บไว้<br>
<img width="1460" height="614" alt="545380104-1d2408df-f937-43a2-9ca1-5033d3d8d2a4" src="https://github.com/user-attachments/assets/6131491f-a9b2-4bbc-a418-d0417b470bba" />
<br>
<br>
<br>
7. ให้คุณไปสร้าง Lightning Invoice ของคุณมาโดยที่ห้ามเกินวงเงินที่ Bolt Card มีและห้ามเกินขนาดของ Max Transaction<br>
(วิธีการเช็ควงเงินให้ใช้คำสั่ง /api/v1/wallet หรือใช้ python ที่มีชื่อ Get_Amount.py)

   ![LN Invoice](https://github.com/user-attachments/assets/965f1a74-3ca1-4d51-9b80-19515fa2a605)
<br>
<br>
<br>
8.จากนั้นให้เอา Callback และค่า k1 ที่ได้จากข้อ 6 มาประกอบกับ Invoice ของคุณซึ่งเป็นสถานที่ที่ต้องการให้เงินไปมาประกอบกัน<br>
ตามสูตรนี้ callback?k1=...&pr=...<br>
<img width="1225" height="691" alt="545380486-121cad91-b634-4976-9db5-fd70d00ac70e" src="https://github.com/user-attachments/assets/1e150ce7-f56d-415e-ae15-f0b841b9d4c7" />

<br>
<br>
<br>
https://YOUR_LN_NODE_URL/boltcards/api/v1/lnurl/cb/k1<br>
  ?k1=....<br>
  &pr=lnbc1....<br>
<br>
<br>
<br>
9.แล้วก็เอา Link ที่เราประกอบกันขึ้นมาไป Browse กับ Google Chrome อีกรอบนึง หากแดกเงินสำเร็จมันจะขึ้นว่า {"status":"OK"}<br>
<img width="799" height="315" alt="545382012-f994505b-6a4f-4d05-ad47-54ef5d8b1a69" src="https://github.com/user-attachments/assets/9ee1d1e1-13ad-4541-8f08-afe9bc456b98" />

   ![Done 1](https://github.com/user-attachments/assets/25a3d825-18fa-44d7-a926-beb2d2e68a03)

   ![Done 2](https://github.com/user-attachments/assets/5161e8d1-a005-42a8-980b-89b8366136f1)
<br>
<img width="1243" height="554" alt="545382151-2c1e0fb0-5e5a-4252-a555-b17d29b9ad4a" src="https://github.com/user-attachments/assets/28f1ef9d-9cb5-4152-b75e-242b4a1a9cc0" />
<br>
<br>
<br>
<br>
ปล. K1 ของ Bolt Card กับ k1 ที่ LNbits Gen ออกมานั้นไม่เหมือนกัน<br>
<img width="794" height="167" alt="K1 is not K1" src="https://github.com/user-attachments/assets/3ef1fe20-2a06-4ac5-bcb0-29530380c14d" />
