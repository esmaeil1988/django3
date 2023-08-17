from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    l=[
        {"onvan":"سیاسی","matn":"ابراهیم رئیسی حمله تروریستی شاهچراغ را محکوم کرد"},
        {"onvan":"اقتصادی","matn":"دلار وارد کانال 47 هزار تومان شد"},
        {"onvan":"ورزشی","matn":"خداحافظی تلخ دیگر در پرسپولیس"},
        {"onvan":"تکنولوژی","matn":"پایتون به عنوان بهترین زبان برنامه نویسی در سال 2023 انتخاب شد"},
        {"onvan":"علمی","matn":"سیگنال عجیب از منبع فرازمینی کشف شد"},
    ]
    return render(request,"news/index.html",context={"esi":l})