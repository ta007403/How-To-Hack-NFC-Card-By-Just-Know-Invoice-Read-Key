วิธีการ Hack เงินจากผู้ให้บริการ NFC Bolt Card\\
\\
วิธีการ Hack Bolt Card ก็ไม่มีอะไรยาก นั่นก็คือการใช้ API ที่ LNBits มีให้นั่นแหละ\\
<img width="1920" height="590" alt="2  LNbits API Document" src="https://github.com/user-attachments/assets/ea4e2915-b383-4e2f-8e5a-033fa378dd57" />
\\
<img width="1446" height="818" alt="3  Bolt Card API Document" src="https://github.com/user-attachments/assets/d68c7bcd-6105-4143-b3ec-3770a6dd3e1a" />
\\
1.หาวิธีให้ได้มาซึ่ง Invoice/Read Key และ Lightning Node URL ของ Account LNbits ที่ Bolt Card นั้นลงทะเบียนอยู่\\
<img width="1221" height="709" alt="1  How toget Invoice read key" src="https://github.com/user-attachments/assets/a06e22b1-bb2f-488c-a23c-aa1872ed8fd2" />
\\
2.จากนั้นทำการยิง API ไปหา Node ด้วยคำสั่งนี้ /boltcards/api/v1/cards [ขั้นตอนนี้คุณสามารถใช้ Code python ที่มีชื่อว่า Get_Data.py ในการดูดข้อมูลได้เลย]\\
<img width="1412" height="692" alt="4  Get Bolt Card Data" src="https://github.com/user-attachments/assets/eb27e358-ffb7-4c40-a420-39532ec73b90" />
\\
3.คุณจะได้มาซึ่งข้อมูลที่จำเป็นในการดูดเงินออกจาก Bolt Card นั่นก็คือ\\
UID\\
Counter Number\\
External ID\\
K1\\
K2\\
\\
4.จากนั้นให้คุณเอาข้อมูลที่ได้มาไปคำนวณหา SUN และ CMAC แล้วก็เอาทั้ง 2 ค่าไปประกอบเป็น  [ขั้นตอนนี้คุณสามารถใช้ Code python ที่มีชื่อว่า Cal_CMAC_SUN.py ในการสร้าง LNURLw ได้เลย]\\
<img width="1411" height="693" alt="6  Cal CMAC and SUN" src="https://github.com/user-attachments/assets/1dde2cdb-e83b-4809-8789-6fb1d962b339" />
\\
5.เมื่อคุณได้ LNURLw มาแล้ว ก็ให้เอาไป Browse ที่ Google Chrome\\
<img width="778" height="678" alt="7  Copy LNURLw" src="https://github.com/user-attachments/assets/e4915bbb-a966-44f8-a2e3-6ca8adc783a4" />
\\
6.จากนั้นให้คุณทำการ Copy ในส่วนของ Callback และค่า k1 ที่ถูก Generate มาจาก LNbits แล้วเก็บไว้\\
<img width="1460" height="614" alt="8  Browse LNURLw" src="https://github.com/user-attachments/assets/1d2408df-f937-43a2-9ca1-5033d3d8d2a4" />
\\
7.ให้คุณไปสร้าง Lightning Invoice ของคุณมาโดยที่ห้ามเกินวงเงินที่ Bolt Card มีและห้ามเกินขนาดของ Max Transaction (วิธีการเช็ควงเงินให้ใช้คำสั่ง /api/v1/wallet เพียงเท่านี้ก็เห็นยอดเงินทั้งบัญชีแล้ว คุณสามารถใช้ python ที่มีชื่อ Get_Amount.py)\\
![LN Invoice](https://github.com/user-attachments/assets/965f1a74-3ca1-4d51-9b80-19515fa2a605)
\\
<img width="1225" height="691" alt="9  Compose" src="https://github.com/user-attachments/assets/121cad91-b634-4976-9db5-fd70d00ac70e" />
\\
8.จากนั้นให้เอา Callback และค่า k1 ที่ได้จากข้อ 6 มาประกอบกับ Invoice ของคุณซึ่งเป็นสถานที่ที่ต้องการให้เงินไปมาประกอบกันตามสูตรนี้ callback?k1=...&pr=...\\

https://YOUR_LN_NODE_URL/boltcards/api/v1/lnurl/cb/k1\\
  ?k1=....\\
  &pr=lnbc1....\\
\\
  หากแดกเงินสำเร็จมันจะขึ้นว่า {"status":"OK"}\\

  ปล. K1 ของ Bolt Card กับ k1 ที่ LNbits Gen ออกมานั้นไม่เหมือนกัน
  <img width="794" height="167" alt="K1 is not K1" src="https://github.com/user-attachments/assets/3ef1fe20-2a06-4ac5-bcb0-29530380c14d" />
