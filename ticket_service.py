from states import ClosedState
from logger import TicketLogger


class TicketService:
    """
    سرویس مدیریت تیکت.
    
    این کلاس:
    - استراتژی‌های ارجاع و پاسخ را نگه می‌دارد (Strategy Pattern)
    - چرخه‌ی وضعیت‌های تیکت را مدیریت می‌کند (State Pattern)
    - در پایان پردازش، رویداد را ثبت می‌کند (Logging)
    """

    def __init__(self, assignment_strategy, response_strategy):
        """
        سازنده سرویس.
        استراتژی‌های مناسب از بیرون تزریق می‌شوند (Dependency Injection).
        """
        # استراتژی تصمیم‌گیری در مورد ارجاع تیکت
        self.assignment_strategy = assignment_strategy
        # استراتژی ارسال پاسخ به کاربر
        self.response_strategy = response_strategy
        # شیء لاگر برای ثبت رویدادها
        self.logger = TicketLogger()

    def handle(self, ticket) -> None:
        """
        تیکت را از ابتدا تا انتها پردازش می‌کند.
        در هر مرحله، وضعیت فعلی تیکت مشخص می‌کند چه اتفاقی بیفتد.
        """
        print(f"\n{'─' * 50}")
        print(f"🎫 شروع پردازش تیکت #{ticket.ticket_id}")
        print(f"{'─' * 50}")

        # حلقه‌ی پردازش: تا زمانی که تیکت به CLOSED نرسیده، مراحل را ادامه بده
        while not isinstance(ticket.get_state(), ClosedState):
            current_state = ticket.get_state()
            print(f"\n▶ وضعیت فعلی: [{current_state.name}]")

            # اجرای رفتار وضعیت فعلی
            current_state.handle(ticket, self)

        # آخرین وضعیت (CLOSED) هم باید handle شود
        ticket.get_state().handle(ticket, self)

        # ثبت لاگ نهایی
        self.logger.log(ticket)

        print(f"{'─' * 50}\n")
