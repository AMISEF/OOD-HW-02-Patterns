from factory import TicketFactory
from ticket_service import TicketService


def main():
    print("=" * 55)
    print("  سیستم مدیریت درخواست‌های پشتیبانی")
    print("  (بازطراحی با الگوهای State, Strategy, Factory)")
    print("=" * 55)

    
    # مثال ۱: تیکت باگ از کانال وب
    print("\n\n📌 مثال ۱: باگ از کانال وب")

    # Factory تیکت و استراتژی‌های مناسب را می‌سازد
    ticket1, assignment1, response1 = TicketFactory.create(
        ticket_id=1,
        channel="WEB",
        ticket_type="BUG"
    )
    ticket1.request = "یک باگ بسیار بد پیدا کردم!"

    # سرویس با استراتژی‌های تزریق‌شده ساخته می‌شود
    service1 = TicketService(
        assignment_strategy=assignment1,
        response_strategy=response1
    )
    service1.handle(ticket1)

    
    # مثال ۲: تیکت پشتیبانی از کانال ایمیل
    print("\n\n📌 مثال ۲: درخواست پشتیبانی از ایمیل")

    ticket2, assignment2, response2 = TicketFactory.create(
        ticket_id=2,
        channel="EMAIL",
        ticket_type="SUPPORT"
    )
    ticket2.request = "چطور می‌توانم تنظیمات حساب کاربری را تغییر دهم؟"

    service2 = TicketService(
        assignment_strategy=assignment2,
        response_strategy=response2
    )
    service2.handle(ticket2)

    
    # مثال ۳: تیکت باگ از ایمیل
    print("\n\n📌 مثال ۳: باگ از کانال ایمیل")

    ticket3, assignment3, response3 = TicketFactory.create(
        ticket_id=3,
        channel="EMAIL",
        ticket_type="BUG"
    )
    ticket3.request = "صفحه‌ی ورود به سیستم کار نمی‌کند."

    service3 = TicketService(
        assignment_strategy=assignment3,
        response_strategy=response3
    )
    service3.handle(ticket3)

    print("\n" + "=" * 55)
    print("  پایان اجرای سیستم")
    print("=" * 55)


if __name__ == "__main__":
    main()
