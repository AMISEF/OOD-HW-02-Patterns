class Ticket:
    """
    کلاس Ticket اطلاعات مربوط به یک درخواست پشتیبانی را نگه‌داری می‌کند.
    این کلاس با الگوی State کار می‌کند؛ یعنی وضعیت (state) از بیرون تزریق می‌شود.
    """

    def __init__(self, ticket_id: int, channel: str, ticket_type: str):
        # شناسه‌ی یکتا برای هر تیکت
        self.ticket_id = ticket_id
        # کانال ورودی: مثلاً "WEB" یا "EMAIL"
        self.channel = channel
        # نوع درخواست: مثلاً "BUG" یا "SUPPORT"
        self.ticket_type = ticket_type
        # متن درخواست کاربر
        self.request: str = ""
        # متن پاسخ سیستم
        self.response: str = ""
        # وضعیت فعلی تیکت (از بیرون تنظیم می‌شود)
        self._state = None

    def set_state(self, state):
        """تنظیم وضعیت فعلی تیکت"""
        self._state = state

    def get_state(self):
        """دریافت وضعیت فعلی تیکت"""
        return self._state

    def get_status_name(self) -> str:
        """نام وضعیت فعلی را برمی‌گرداند"""
        if self._state:
            return self._state.name
        return "UNKNOWN"

    def __repr__(self):
        return (
            f"Ticket(id={self.ticket_id}, "
            f"channel='{self.channel}', "
            f"type='{self.ticket_type}', "
            f"status='{self.get_status_name()}')"
        )
