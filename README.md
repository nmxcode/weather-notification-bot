

# ربات اطلاع‌رسانی آب‌وهوا (Weather Notification Bot)

این پروژه با Python و برنامه‌نویسی شیءگرا (OOP) نوشته شده است.

برنامه اطلاعات آب‌وهوای شهر انتخاب‌شده را از Open-Meteo دریافت می‌کند، داده‌ها را به‌صورت JSON آماده می‌کند و آن‌ها را با درخواست POST به Postman Echo و Webhook.site می‌فرستد.

## قابلیت‌ها

1. دریافت نام شهر از کاربر
2. جست‌وجوی شهر و دریافت مختصات با Geocoding API از Open-Meteo
3. دریافت اطلاعات فعلی آب‌وهوا با Weather API
4. تبدیل کد وضعیت هوا به توضیح متنی
5. ساخت داده نهایی در قالب Dictionary/JSON
6. ارسال داده همراه با هدر Authorization به Postman Echo
7. ارسال همان داده به Webhook.site
8. بررسی پاسخ Postman Echo و نمایش وضعیت درخواست‌ها

## ساختار کلاس‌ها

پروژه حداکثر سه کلاس دارد:

| کلاس | مسئولیت |
|---|---|
| WeatherClient | جست‌وجوی شهر و دریافت اطلاعات آب‌وهوا از Open-Meteo |
| ApiSender | ساخت Header و ارسال درخواست POST به Postman Echo و Webhook.site |
| WeatherBot | هماهنگ‌کردن مراحل و اجرای کل برنامه |

### متدهای WeatherClient

- `search_city(city_name)`: جست‌وجوی شهر و برگرداندن نتایج.
- `get_weather(place)`: دریافت وضعیت فعلی هوا و برگرداندن داده‌ها به شکل Dictionary.

### متدهای ApiSender

- `send_post(url, data)`: ارسال عمومی درخواست POST با JSON و Headerها.
- `send_to_postman(data)`: ارسال داده به Postman Echo و بررسی تطابق JSON دریافتی.
- `send_to_webhook(webhook_url, data)`: اعتبارسنجی URL و ارسال داده به Webhook.site.

### متد WeatherBot

- `run()`: دریافت ورودی کاربر، انتخاب شهر، دریافت آب‌وهوا و ارسال داده به دو مقصد.

## پیش‌نیازها

- Python 3.10 یا بالاتر
- دسترسی به اینترنت
- یک URL اختصاصی از Webhook.site
- پکیج requests

ماژول‌های json و urllib.parse جزو کتابخانه استاندارد Python هستند و نیاز به نصب جداگانه ندارند.

## نصب وابستگی‌ها

ابتدا محیط Conda پروژه را فعال کن:

```bash
conda activate lern-py
```

سپس از پوشه اصلی پروژه دستور زیر را اجرا کن:

```bash
python -m pip install -r requirements.txt
```

اگر پکیج requests از قبل در محیط نصب است، نصب مجدد آن لازم نیست.

## اجرای برنامه

کد سه کلاس و بخش اجرای اصلی را در فایلی با نام `weather_bot.py` ذخیره کن.

از Terminal وارد پوشه‌ای شو که فایل در آن قرار دارد و اجرا کن:

```bash
python weather_bot.py
```

برنامه نام شهر را درخواست می‌کند. نام شهر را ترجیحاً به انگلیسی وارد کن؛ برای مثال:

```text
Tehran
```

اگر چند نتیجه پیدا شود، فهرست شهرها نمایش داده می‌شود. شماره شهر موردنظر را وارد کن.

## تنظیم Webhook و API Key

در انتهای فایل `weather_bot.py` این مقادیر تنظیم شده‌اند:

```python
API_KEY = "MY_TEST_API_KEY_123"

WEBHOOK_URL = (
    "https://webhook.site/"
    "YOUR-UNIQUE-ID"
)
```

مقدار WEBHOOK_URL را با URL اختصاصی خودت از Webhook.site جایگزین کن.

**نکته امنیتی:** URL اختصاصی Webhook.site را عمومی نکن. هر فردی که این URL را داشته باشد می‌تواند برای آن درخواست ارسال کند. از کلید واقعی یا محرمانه در این تمرین استفاده نکن.

## روش بررسی نتیجه

### 1. بررسی Postman Echo

برنامه داده را به آدرس زیر ارسال می‌کند:

https://postman-echo.com/post

در پاسخ، JSON ارسال‌شده و Headerهای درخواست برگردانده می‌شوند.

برنامه بررسی می‌کند که مقدار JSON برگشتی با داده ارسالی برابر باشد.

توجه: Postman Echo فقط دریافت Header را بازتاب می‌دهد و کلید آزمایشی را اعتبارسنجی نمی‌کند.

### 2. بررسی Webhook.site

1. وارد https://webhook.site/ شو.
2. درخواست جدید را از فهرست درخواست‌ها انتخاب کن.
3. در بخش Request Content یا Raw Content، داده JSON را بررسی کن.
4. در بخش Request Details & Headers، هدر authorization را بررسی کن.
5. از صفحه درخواست دریافتی Screenshot بگیر.

## نمونه داده ارسالی

مقادیر زیر فقط نمونه هستند. داده واقعی بر اساس پاسخ API و زمان اجرای برنامه تغییر می‌کند.

```json
{
  "city": "Tehran",
  "country": "Iran",
  "latitude": 35.69439,
  "longitude": 51.42151,
  "temperature": 13.1,
  "feels_like": 10.5,
  "humidity": 37,
  "wind_speed": 1.8,
  "precipitation": 0,
  "weather_code": 0,
  "weather_description": "صاف",
  "is_day": 0,
  "time": "2026-11-17T18:15",
  "timezone": "Asia/Tehran"
}
```

## مدیریت خطا

برنامه خطاهای HTTP را با `raise_for_status()` بررسی می‌کند.

در بخش اجرای اصلی نیز خطاهای درخواست و ورودی‌های نامعتبر مدیریت می‌شوند.

خطاهای احتمالی:

- نام شهر پیدا نشود.
- شماره انتخاب شهر معتبر نباشد.
- اتصال اینترنت یا API در دسترس نباشد.
- URL وب‌هوک معتبر نباشد.
- سرور مقصد پاسخ خطا برگرداند.

## چک‌لیست تحویل تمرین

- [ ] فایل weather_bot.py
- [ ] فایل requirements.txt
- [ ] فایل README.md
- [ ] اجرای موفق دریافت اطلاعات با GET
- [ ] مشاهده داده ارسالی در پاسخ Postman Echo
- [ ] مشاهده درخواست در Webhook.site
- [ ] Screenshot از Request Body و Headers در Webhook.site

## توضیح کوتاه پروژه برای گزارش

در این پروژه، نام شهر از کاربر دریافت شد و با استفاده از Geocoding API در Open-Meteo مختصات آن پیدا شد. سپس اطلاعات فعلی آب‌وهوا با درخواست GET دریافت و داده‌های موردنیاز در قالب JSON آماده شد. در ادامه، داده‌ها با درخواست POST و هدر Authorization به Postman Echo ارسال شدند. در پایان، همان داده‌ها به Webhook.site ارسال و دریافت آن‌ها در پنل سایت بررسی شد.