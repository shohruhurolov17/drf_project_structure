DRF Project Structure
Bu repository Django Rest Framework (DRF) asosida qurilgan loyihalar uchun standart struktura sifatida xizmat qiladi. Ushbu shablon yordamida siz API-ga asoslangan loyihalarni tez va samarali boshlashingiz mumkin. Struktura toza kod yozish, modulli dizayn va oson kengaytirilishi uchun optimallashtirilgan.

1. Reponi klon qilib olish

```
git clone https://github.com/shohruhurolov17/drf_project_structure.git
cd drf_project_structure
```


2. Virtual muhit yaratish va uni faollashtirish.

```
python3 -m venv venv 
source venv/bin/activate #Linux/Mac
venv\Scripts\activate #Windows
```


3. Kerakli paketlarni o'rnatish

```
pip install -r requirements/dev.txt
```


4.Atrof-muhit o'zgaruvchilarini sozlash:
.env.example faylini .env ga nusxalang va kerakli qiymatlarni kiriting:

```
cp .example.env .env
```


5.Migratsiyalarni amalga oshirish

```
python3 manage.py makemigrations
python3 manage.py migrate
```


6.Serverni ishga tushiring

```
python3 manage.py runserver
```
#Default holatda server http://localhost:8000 manzilda ishlaydi.



