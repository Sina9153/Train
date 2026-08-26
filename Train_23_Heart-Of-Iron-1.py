import tkinter as tk
from tkinter import messagebox
import random
import math


# =========================================================
# MINI HEARTS OF IRON
# نسخه یکپارچه:
# - نقشه
# - انتخاب کشور
# - کارخانه غیرنظامی
# - کارخانه نظامی
# - خطوط تولید
# - تفنگ
# - توپخانه
# - تانک
# - نیروی انسانی
# - تحقیق
# - ساخت ارتش
# - جنگ
# - هوش مصنوعی
# - تاریخ
# =========================================================


WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 850

MAP_WIDTH = 800
MAP_HEIGHT = 780

PANEL_WIDTH = 420


# =========================================================
# COUNTRY CLASS
# =========================================================

class Country:

    def __init__(
        self,
        name,
        color,
        x,
        y,
        width,
        height,
        manpower,
        civilian_factories,
        military_factories
    ):

        self.name = name
        self.color = color

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        # -------------------------
        # منابع
        # -------------------------

        self.manpower = manpower

        # -------------------------
        # کارخانه‌ها
        # -------------------------

        self.civilian_factories = civilian_factories
        self.military_factories = military_factories

        # -------------------------
        # تجهیزات
        # -------------------------

        self.rifles = 100
        self.artillery = 20
        self.tanks = 5

        # -------------------------
        # ارتش
        # -------------------------

        self.army = 10

        # -------------------------
        # سیاست
        # -------------------------

        self.stability = 70
        self.war_support = 50

        # -------------------------
        # تحقیق
        # -------------------------

        self.research_points = 0

        self.infantry_tech = 1
        self.artillery_tech = 1
        self.tank_tech = 1

        # -------------------------
        # ساخت‌وساز
        # -------------------------

        self.construction_type = None
        self.construction_progress = 0

        # -------------------------
        # خطوط تولید
        # -------------------------

        self.production_rifles = 0
        self.production_artillery = 0
        self.production_tanks = 0

        # -------------------------
        # مالک
        # -------------------------

        self.owner = name

    def center(self):

        return (
            self.x + self.width / 2,
            self.y + self.height / 2
        )

    def total_equipment(self):

        return (
            self.rifles
            + self.artillery * 2
            + self.tanks * 5
        )


# =========================================================
# GAME
# =========================================================

class MiniHOI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Mini Hearts of Iron"
        )

        # اجرای بازی به صورت تمام صفحه
        self.root.state("zoomed")

        self.root.resizable(True,True)


        # -------------------------
        # تاریخ
        # -------------------------

        self.day = 1
        self.month = 1
        self.year = 1936

        # -------------------------
        # کشور بازیکن
        # -------------------------

        self.player = None

        # -------------------------
        # کشور انتخاب‌شده
        # -------------------------

        self.selected_country = None

        # -------------------------
        # پایان بازی
        # -------------------------

        self.game_over = False

        # -------------------------
        # کشورها
        # -------------------------

        self.countries = {}

        self.create_countries()

        self.create_ui()

        self.draw_map()

        self.update_info()

    # =====================================================
    # CREATE COUNTRIES
    # =====================================================

    def create_countries(self):

        self.countries["Britain"] = Country(
            "Britain",
            "#8064A2",
            55,
            145,
            145,
            115,
            120,
            15,
            10
        )

        self.countries["France"] = Country(
            "France",
            "#3F73C9",
            200,
            355,
            170,
            125,
            70,
            10,
            8
        )

        self.countries["Germany"] = Country(
            "Germany",
            "#666666",
            375,
            235,
            165,
            120,
            80,
            18,
            14
        )

        self.countries["Poland"] = Country(
            "Poland",
            "#F2F2F2",
            540,
            270,
            125,
            105,
            35,
            5,
            4
        )

        self.countries["Italy"] = Country(
            "Italy",
            "#2F8F55",
            400,
            485,
            120,
            120,
            50,
            8,
            7
        )

        self.countries["USSR"] = Country(
            "USSR",
            "#B52B2B",
            665,
            145,
            110,
            290,
            180,
            25,
            18
        )

    # =====================================================
    # CREATE UI
    # =====================================================

    def create_ui(self):

        # =================================================
        # MAP
        # =================================================

        self.canvas = tk.Canvas(
            self.root,
            width=MAP_WIDTH,
            height=MAP_HEIGHT,
            bg="#17351F",
            highlightthickness=0
        )

        self.canvas.pack(
            side=tk.LEFT
        )

        self.canvas.bind(
            "<Button-1>",
            self.click_map
        )

        # =================================================
        # PANEL
        # =================================================

        self.panel = tk.Frame(
            self.root,
            width=PANEL_WIDTH,
            height=MAP_HEIGHT,
            bg="#202020"
        )

        self.panel.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        self.panel.pack_propagate(False)

        # =================================================
        # TITLE
        # =================================================

        tk.Label(
            self.panel,
            text="MINI HEARTS OF IRON",
            fg="white",
            bg="#202020",
            font=("Arial", 16, "bold")
        ).pack(
            pady=(12, 4)
        )

        # =================================================
        # PLAYER
        # =================================================

        self.player_label = tk.Label(
            self.panel,
            text="کشور شما: انتخاب نشده",
            fg="#FFD700",
            bg="#202020",
            font=("Arial", 11, "bold")
        )

        self.player_label.pack(
            pady=3
        )

        # =================================================
        # DATE
        # =================================================

        self.date_label = tk.Label(
            self.panel,
            text="",
            fg="#5CFFB0",
            bg="#202020",
            font=("Arial", 11, "bold")
        )

        self.date_label.pack(
            pady=3
        )

        # =================================================
        # TABS
        # =================================================

        tab_frame = tk.Frame(
            self.panel,
            bg="#202020"
        )

        tab_frame.pack(
            fill=tk.X,
            padx=10,
            pady=5
        )

        self.overview_button = tk.Button(
            tab_frame,
            text="اطلاعات",
            command=self.show_overview,
            bg="#444444",
            fg="white"
        )

        self.overview_button.pack(
            side=tk.LEFT,
            expand=True,
            fill=tk.X
        )

        self.economy_button = tk.Button(
            tab_frame,
            text="اقتصاد",
            command=self.show_economy,
            bg="#333333",
            fg="white"
        )

        self.economy_button.pack(
            side=tk.LEFT,
            expand=True,
            fill=tk.X
        )

        self.production_button = tk.Button(
            tab_frame,
            text="تولید",
            command=self.show_production,
            bg="#333333",
            fg="white"
        )

        self.production_button.pack(
            side=tk.LEFT,
            expand=True,
            fill=tk.X
        )

        # =================================================
        # INFO
        # =================================================

        self.info_label = tk.Label(
            self.panel,
            text="برای شروع یک کشور را انتخاب کنید.",
            fg="white",
            bg="#202020",
            justify=tk.LEFT,
            anchor="nw",
            font=("Arial", 9)
        )

        self.info_label.pack(
            padx=15,
            pady=5,
            fill=tk.X
        )
        # =====================================================
        # REPORT FRAME
        # =====================================================

        report_frame = tk.Frame(
            self.panel,
            bg="#202020"
        )

        report_frame.pack(
            padx=10,
            pady=(8, 2),
            fill=tk.BOTH,
            expand=True
        )

        tk.Label(
            report_frame,
            text="📜 گزارش بازی",
            fg="#FFD700",
            bg="#202020",
            font=("Arial", 10, "bold")
        ).pack(
            pady=3
        )

        log_box_frame = tk.Frame(
            report_frame,
            bg="#111111"
        )

        log_box_frame.pack(
            fill=tk.BOTH,
            expand=True
        )

        self.log = tk.Text(
            log_box_frame,
            bg="#111111",
            fg="#DDDDDD",
            insertbackground="white",
            font=("Arial", 9),
            wrap=tk.WORD,
            relief=tk.FLAT
        )

        self.log.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        log_scroll = tk.Scrollbar(
            log_box_frame,
            command=self.log.yview
        )

        log_scroll.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        self.log.config(
            yscrollcommand=log_scroll.set
        )


        # =================================================
        # BUILD ARMY
        # =================================================

        tk.Button(
            self.panel,
            text="🪖 ساخت لشکر",
            command=self.build_army,
            bg="#444444",
            fg="white"
        ).pack(
            padx=20,
            pady=3,
            fill=tk.X
        )

        # =================================================
        # ATTACK
        # =================================================

        tk.Button(
            self.panel,
            text="⚔️ حمله",
            command=self.attack,
            bg="#8B0000",
            fg="white"
        ).pack(
            padx=20,
            pady=3,
            fill=tk.X
        )

        # =================================================
        # MILITARY FACTORY
        # =================================================

        tk.Button(
            self.panel,
            text="🏭 ساخت کارخانه نظامی",
            command=self.start_military_factory,
            bg="#705000",
            fg="white"
        ).pack(
            padx=20,
            pady=3,
            fill=tk.X
        )

        # =================================================
        # CIVILIAN FACTORY
        # =================================================

        tk.Button(
            self.panel,
            text="🏗 ساخت کارخانه غیرنظامی",
            command=self.start_civilian_factory,
            bg="#505050",
            fg="white"
        ).pack(
            padx=20,
            pady=3,
            fill=tk.X
        )

        # =================================================
        # RESEARCH
        # =================================================

        tk.Button(
            self.panel,
            text="🔬 تحقیق",
            command=self.research,
            bg="#304A70",
            fg="white"
        ).pack(
            padx=20,
            pady=3,
            fill=tk.X
        )

        # =================================================
        # NEXT DAY
        # =================================================

        tk.Button(
            self.panel,
            text="▶ روز بعد",
            command=self.next_day,
            bg="#31572C",
            fg="white",
            font=("Arial", 10, "bold")
        ).pack(
            padx=20,
            pady=7,
            fill=tk.X
        )

        # =================================================
        # LOG
        # =================================================

        tk.Label(
            self.panel,
            text="گزارش بازی",
            fg="white",
            bg="#202020"
        ).pack(
            pady=(5, 2)
        )

        self.log = tk.Text(
            self.panel,
            height=12,
            bg="#111111",
            fg="#DDDDDD",
            font=("Arial", 8)
        )

        self.log.pack(
            padx=10,
            pady=3,
            fill=tk.BOTH,
            expand=True
        )

        self.log_message(
            "برای شروع روی یک کشور کلیک کنید."
        )

    # =====================================================
    # DRAW MAP
    # =====================================================

    def draw_map(self):

        self.canvas.delete("all")

        # -------------------------
        # background
        # -------------------------

        self.canvas.create_rectangle(
            0,
            0,
            MAP_WIDTH,
            MAP_HEIGHT,
            fill="#17351F",
            outline=""
        )

        # -------------------------
        # sea
        # -------------------------

        self.canvas.create_rectangle(
            0,
            0,
            MAP_WIDTH,
            105,
            fill="#183A52",
            outline=""
        )

        self.canvas.create_text(
            MAP_WIDTH / 2,
            50,
            text="EUROPE - 1936",
            fill="#A9D6E5",
            font=("Arial", 23, "bold")
        )

        # -------------------------
        # grid
        # -------------------------

        for x in range(
            0,
            MAP_WIDTH,
            50
        ):

            self.canvas.create_line(
                x,
                105,
                x,
                MAP_HEIGHT,
                fill="#21432B"
            )

        for y in range(
            105,
            MAP_HEIGHT,
            50
        ):

            self.canvas.create_line(
                0,
                y,
                MAP_WIDTH,
                y,
                fill="#21432B"
            )

        # -------------------------
        # countries
        # -------------------------

        for country in self.countries.values():

            owner = self.countries.get(
                country.owner
            )

            if owner:
                color = owner.color
            else:
                color = country.color

            if country == self.player:

                border = "#FFD700"
                border_width = 5

            elif country == self.selected_country:

                border = "#00FFFF"
                border_width = 4

            else:

                border = "#111111"
                border_width = 2

            # کشور

            self.canvas.create_rectangle(
                country.x,
                country.y,
                country.x + country.width,
                country.y + country.height,
                fill=color,
                outline=border,
                width=border_width
            )

            text_color = (
                "black"
                if country.name == "Poland"
                else "white"
            )

            # نام

            self.canvas.create_text(
                country.x + country.width / 2,
                country.y + country.height / 2 - 25,
                text=country.name,
                fill=text_color,
                font=("Arial", 10, "bold")
            )

            # ارتش

            self.canvas.create_text(
                country.x + country.width / 2,
                country.y + country.height / 2 - 3,
                text=f"Army: {country.army}",
                fill=text_color
            )

            # کارخانه

            self.canvas.create_text(
                country.x + country.width / 2,
                country.y + country.height / 2 + 18,
                text=(
                    f"C:{country.civilian_factories} "
                    f"M:{country.military_factories}"
                ),
                fill=text_color,
                font=("Arial", 8)
            )

        # -------------------------
        # legend
        # -------------------------

        self.canvas.create_text(
            15,
            MAP_HEIGHT - 20,
            text=(
                "زرد = کشور شما   "
                "آبی = هدف   "
                "C = غیرنظامی   "
                "M = نظامی"
            ),
            anchor="w",
            fill="white",
            font=("Arial", 8)
        )

    # =====================================================
    # CLICK MAP
    # =====================================================

    def click_map(self, event):

        clicked = None

        for country in self.countries.values():

            if (
                country.x <= event.x <= country.x + country.width
                and
                country.y <= event.y <= country.y + country.height
            ):

                clicked = country
                break

        if clicked is None:
            return

        # -------------------------
        # انتخاب کشور برای شروع
        # -------------------------

        if self.player is None:

            answer = messagebox.askyesno(
                "انتخاب کشور",
                f"آیا می‌خواهید با {clicked.name} بازی کنید؟"
            )

            if answer:

                self.player = clicked
                self.selected_country = clicked

                self.player_label.config(
                    text=f"کشور شما: {clicked.name}"
                )

                self.log_message(
                    f"🇺🇳 {clicked.name} انتخاب شد."
                )

                self.log_message(
                    "🎮 بازی شروع شد!"
                )

                self.update_info()
                self.draw_map()

            return

        # -------------------------
        # بعد از شروع بازی
        # -------------------------

        self.selected_country = clicked

        self.log_message(
            f"🎯 انتخاب شد: {clicked.name}"
        )

        self.update_info()
        self.draw_map()

    # =====================================================
    # UPDATE INFO
    # =====================================================

    def update_info(self):

        # تاریخ

        self.date_label.config(
            text=(
                f"📅 "
                f"{self.day:02d}/"
                f"{self.month:02d}/"
                f"{self.year}"
            )
        )

        # اگر کشور انتخاب نشده

        if self.selected_country is None:

            self.info_label.config(
                text="برای شروع یک کشور را انتخاب کنید."
            )

            return

        c = self.selected_country

        # -------------------------
        # تجهیزات
        # -------------------------

        total_equipment = c.total_equipment()

        # -------------------------
        # ساخت و ساز
        # -------------------------

        construction = "هیچ پروژه‌ای در حال ساخت نیست."

        if c.construction_type == "military":

            construction = (
                f"🏭 کارخانه نظامی: "
                f"{c.construction_progress}%"
            )

        elif c.construction_type == "civilian":

            construction = (
                f"🏗 کارخانه غیرنظامی: "
                f"{c.construction_progress}%"
            )

        # -------------------------
        # متن
        # -------------------------

        text = (
            f"🌍 کشور: {c.name}\n\n"

            f"🪖 ارتش: {c.army}\n"
            f"👥 نیروی انسانی: {c.manpower}\n\n"

            f"🏭 کارخانه غیرنظامی: "
            f"{c.civilian_factories}\n"

            f"⚔ کارخانه نظامی: "
            f"{c.military_factories}\n\n"

            f"🔫 تفنگ: {c.rifles}\n"
            f"💥 توپخانه: {c.artillery}\n"
            f"🛡 تانک: {c.tanks}\n"
            f"📦 تجهیزات کل: {total_equipment}\n\n"

            f"🔬 امتیاز تحقیق: "
            f"{c.research_points}\n\n"

            f"📚 پیاده‌نظام: "
            f"{c.infantry_tech}\n"

            f"📚 توپخانه: "
            f"{c.artillery_tech}\n"

            f"📚 تانک: "
            f"{c.tank_tech}\n\n"

            f"📈 ثبات: {c.stability}%\n"
            f"⚔ حمایت جنگی: {c.war_support}%\n\n"

            f"{construction}"
        )

        self.info_label.config(
            text=text
        )

    # =====================================================
    # OVERVIEW
    # =====================================================

    def show_overview(self):

        self.update_info()

    # =====================================================
    # ECONOMY
    # =====================================================

    def show_economy(self):

        if self.selected_country is None:
            return

        c = self.selected_country

        construction = "هیچ پروژه‌ای نیست"

        if c.construction_type:

            construction = (
                f"{c.construction_type} - "
                f"{c.construction_progress}%"
            )

        text = (
            f"🏭 اقتصاد {c.name}\n\n"

            f"🏗 کارخانه غیرنظامی: "
            f"{c.civilian_factories}\n\n"

            f"⚔ کارخانه نظامی: "
            f"{c.military_factories}\n\n"

            f"💰 ظرفیت ساخت‌وساز: "
            f"{c.civilian_factories}\n\n"

            f"🏗 پروژه فعلی:\n"
            f"{construction}\n\n"

            f"👥 نیروی انسانی: "
            f"{c.manpower}\n\n"

            f"📈 ثبات: "
            f"{c.stability}%\n"

            f"⚔ حمایت جنگی: "
            f"{c.war_support}%"
        )

        self.info_label.config(
            text=text
        )

    # =====================================================
    # PRODUCTION
    # =====================================================

    def show_production(self):

        if self.player is None:
            return

        c = self.player

        text = (
            f"🏭 خطوط تولید\n\n"

            f"⚔ کارخانه‌های نظامی: "
            f"{c.military_factories}\n\n"

            f"🔫 تفنگ: "
            f"{c.production_rifles}\n"

            f"💥 توپخانه: "
            f"{c.production_artillery}\n"

            f"🛡 تانک: "
            f"{c.production_tanks}\n\n"

            f"📦 موجودی:\n"

            f"تفنگ: {c.rifles}\n"
            f"توپخانه: {c.artillery}\n"
            f"تانک: {c.tanks}"
        )

        self.info_label.config(
            text=text
        )

        # پنجره تنظیم تولید

        self.production_window()

    # =====================================================
    # PRODUCTION WINDOW
    # =====================================================

    def production_window(self):

        if self.player is None:
            return

        window = tk.Toplevel(
            self.root
        )

        window.title(
            "خطوط تولید"
        )

        window.geometry(
            "360x300"
        )

        window.resizable(
            False,
            False
        )

        tk.Label(
            window,
            text="تعداد کارخانه برای هر محصول",
            font=("Arial", 12, "bold")
        ).pack(
            pady=10
        )

        # -------------------------
        # rifles
        # -------------------------

        tk.Label(
            window,
            text="🔫 تفنگ"
        ).pack()

        rifles_var = tk.IntVar(
            value=self.player.production_rifles
        )

        tk.Spinbox(
            window,
            from_=0,
            to=self.player.military_factories,
            textvariable=rifles_var,
            width=10
        ).pack(
            pady=3
        )

        # -------------------------
        # artillery
        # -------------------------

        tk.Label(
            window,
            text="💥 توپخانه"
        ).pack()

        artillery_var = tk.IntVar(
            value=self.player.production_artillery
        )

        tk.Spinbox(
            window,
            from_=0,
            to=self.player.military_factories,
            textvariable=artillery_var,
            width=10
        ).pack(
            pady=3
        )

        # -------------------------
        # tanks
        # -------------------------

        tk.Label(
            window,
            text="🛡 تانک"
        ).pack()

        tanks_var = tk.IntVar(
            value=self.player.production_tanks
        )

        tk.Spinbox(
            window,
            from_=0,
            to=self.player.military_factories,
            textvariable=tanks_var,
            width=10
        ).pack(
            pady=3
        )

        # -------------------------
        # save
        # -------------------------

        def save_production():

            rifles = max(
                0,
                rifles_var.get()
            )

            artillery = max(
                0,
                artillery_var.get()
            )

            tanks = max(
                0,
                tanks_var.get()
            )

            total = (
                rifles
                + artillery
                + tanks
            )

            if total > self.player.military_factories:

                messagebox.showerror(
                    "خطا",
                    "تعداد کارخانه‌های اختصاص داده‌شده "
                    "از کارخانه‌های نظامی شما بیشتر است."
                )

                return

            self.player.production_rifles = rifles
            self.player.production_artillery = artillery
            self.player.production_tanks = tanks

            self.log_message(
                "🏭 خطوط تولید به‌روزرسانی شدند."
            )

            window.destroy()

            self.show_production()

        tk.Button(
            window,
            text="ذخیره",
            command=save_production,
            bg="#31572C",
            fg="white"
        ).pack(
            pady=15,
            ipadx=30
        )

    # =====================================================
    # BUILD ARMY
    # =====================================================

    def build_army(self):

        if self.player is None:

            messagebox.showwarning(
                "خطا",
                "ابتدا کشور خود را انتخاب کنید."
            )

            return

        c = self.player

        # هزینه

        manpower_cost = 5
        rifle_cost = 20

        if c.manpower < manpower_cost:

            self.log_message(
                "❌ نیروی انسانی کافی نیست."
            )

            return

        if c.rifles < rifle_cost:

            self.log_message(
                "❌ تفنگ کافی نیست."
            )

            return

        c.manpower -= manpower_cost
        c.rifles -= rifle_cost

        c.army += 2

        self.log_message(
            "🪖 ۲ واحد ارتش تشکیل شد."
        )

        self.selected_country = c

        self.update_info()
        self.draw_map()

    # =====================================================
    # START MILITARY FACTORY
    # =====================================================

    def start_military_factory(self):

        if self.player is None:
            return

        c = self.player

        if c.construction_type:

            self.log_message(
                "🏗 یک پروژه دیگر در حال ساخت است."
            )

            return

        if c.civilian_factories < 5:

            self.log_message(
                "❌ حداقل ۵ کارخانه غیرنظامی لازم است."
            )

            return

        c.civilian_factories -= 5

        c.construction_type = "military"

        c.construction_progress = 0

        self.log_message(
            "🏭 ساخت کارخانه نظامی آغاز شد."
        )

        self.update_info()

    # =====================================================
    # START CIVILIAN FACTORY
    # =====================================================

    def start_civilian_factory(self):

        if self.player is None:
            return

        c = self.player

        if c.construction_type:

            self.log_message(
                "🏗 یک پروژه دیگر در حال ساخت است."
            )

            return

        if c.civilian_factories < 3:

            self.log_message(
                "❌ کارخانه غیرنظامی کافی نیست."
            )

            return

        c.civilian_factories -= 3

        c.construction_type = "civilian"

        c.construction_progress = 0

        self.log_message(
            "🏗 ساخت کارخانه غیرنظامی آغاز شد."
        )

        self.update_info()

    # =====================================================
    # RESEARCH
    # =====================================================

    def research(self):

        if self.player is None:
            return

        c = self.player

        cost = 100

        if c.research_points < cost:

            self.log_message(
                "❌ امتیاز تحقیق کافی نیست."
            )

            return

        c.research_points -= cost

        choice = random.choice(
            [
                "infantry",
                "artillery",
                "tank"
            ]
        )

        if choice == "infantry":

            c.infantry_tech += 1

            self.log_message(
                "🔬 تکنولوژی پیاده‌نظام ارتقا یافت!"
            )

        elif choice == "artillery":

            c.artillery_tech += 1

            self.log_message(
                "🔬 تکنولوژی توپخانه ارتقا یافت!"
            )

        else:

            c.tank_tech += 1

            self.log_message(
                "🔬 تکنولوژی تانک ارتقا یافت!"
            )

        self.update_info()

    # =====================================================
    # NEXT DAY
    # =====================================================

    def next_day(self):

        if self.player is None:

            messagebox.showwarning(
                "شروع بازی",
                "ابتدا کشور خود را انتخاب کنید."
            )

            return

        if self.game_over:
            return

        # -------------------------
        # date
        # -------------------------

        self.day += 1

        if self.day > 30:

            self.day = 1
            self.month += 1

        if self.month > 12:

            self.month = 1
            self.year += 1

        # -------------------------
        # player
        # -------------------------

        self.produce_country(
            self.player
        )

        self.construction_tick(
            self.player
        )

        # -------------------------
        # AI
        # -------------------------

        for country in self.countries.values():

            if country != self.player:

                if country.owner == country.name:

                    self.produce_country(
                        country
                    )

                    self.construction_tick(
                        country
                    )

        # -------------------------
        # AI decisions
        # -------------------------

        self.ai_turn()

        self.log_message(
            f"📅 تاریخ: "
            f"{self.day:02d}/"
            f"{self.month:02d}/"
            f"{self.year}"
        )

        self.update_info()

        self.draw_map()

        self.check_victory()

    # =====================================================
    # PRODUCE COUNTRY
    # =====================================================

    def produce_country(
        self,
        country
    ):

        # -------------------------
        # manpower
        # -------------------------

        country.manpower += 1

        # -------------------------
        # research
        # -------------------------

        country.research_points += 8

        # -------------------------
        # production
        # -------------------------

        # rifles

        for _ in range(
            country.production_rifles
        ):

            country.rifles += (
                5
                + country.infantry_tech
            )

        # artillery

        for _ in range(
            country.production_artillery
        ):

            country.artillery += (
                1
                + country.artillery_tech
            )

        # tanks

        for _ in range(
            country.production_tanks
        ):

            if random.random() < 0.5:

                country.tanks += (
                    1
                    + country.tank_tech // 2
                )

    # =====================================================
    # CONSTRUCTION TICK
    # =====================================================

    def construction_tick(
        self,
        country
    ):

        if country.construction_type is None:
            return

        # سرعت ساخت

        speed = min(
            20,
            4
            + country.civilian_factories // 3
        )

        country.construction_progress += speed

        if country.construction_progress >= 100:

            if country.construction_type == "military":

                country.military_factories += 1

                self.log_message(
                    f"🏭 {country.name}: "
                    f"کارخانه نظامی ساخته شد."
                )

            elif country.construction_type == "civilian":

                country.civilian_factories += 1

                self.log_message(
                    f"🏗 {country.name}: "
                    f"کارخانه غیرنظامی ساخته شد."
                )

            country.construction_type = None

            country.construction_progress = 0

    # =====================================================
    # ATTACK
    # =====================================================

    def attack(self):

        if self.player is None:
            return

        if self.selected_country is None:
            return

        attacker = self.player
        target = self.selected_country

        if target == attacker:

            self.log_message(
                "❌ نمی‌توانید به خودتان حمله کنید."
            )

            return

        if target.owner == attacker.name:

            self.log_message(
                "❌ این سرزمین قبلاً تحت کنترل شماست."
            )

            return

        if not self.are_neighbors(
            attacker,
            target
        ):

            self.log_message(
                "❌ این کشور بیش از حد دور است."
            )

            return

        if attacker.army <= 1:

            self.log_message(
                "❌ ارتش کافی ندارید."
            )

            return

        # -------------------------
        # combat power
        # -------------------------

        attacker_power = (
            attacker.army
            * (1 + attacker.infantry_tech * 0.1)
            * random.uniform(
                0.75,
                1.30
            )
        )

        defender_power = (
            target.army
            * (1 + target.infantry_tech * 0.1)
            * random.uniform(
                0.75,
                1.25
            )
        )

        # توپخانه

        attacker_power += (
            attacker.artillery
            * 0.08
        )

        defender_power += (
            target.artillery
            * 0.08
        )

        # تانک

        attacker_power += (
            attacker.tanks
            * 0.35
        )

        defender_power += (
            target.tanks
            * 0.35
        )

        self.log_message(
            f"⚔️ {attacker.name} "
            f"به {target.name} حمله کرد!"
        )

        # -------------------------
        # victory
        # -------------------------

        if attacker_power > defender_power:

            enemy_loss = random.randint(
                2,
                max(
                    3,
                    target.army // 2
                )
            )

            attacker_loss = random.randint(
                1,
                3
            )

            target.army -= enemy_loss

            attacker.army = max(
                1,
                attacker.army - attacker_loss
            )

            attacker.rifles = max(
                0,
                attacker.rifles - 10
            )

            if target.army <= 0:

                target.army = 1

                target.owner = attacker.name

                self.log_message(
                    "🏆 پیروزی!"
                )

                self.log_message(
                    f"🇺🇳 {target.name} فتح شد!"
                )

            else:

                self.log_message(
                    f"دشمن {enemy_loss} "
                    f"واحد از دست داد."
                )

        # -------------------------
        # defeat
        # -------------------------

        else:

            attacker_loss = random.randint(
                2,
                5
            )

            attacker.army = max(
                1,
                attacker.army - attacker_loss
            )

            attacker.rifles = max(
                0,
                attacker.rifles - 15
            )

            self.log_message(
                "❌ حمله شکست خورد!"
            )

            self.log_message(
                f"{attacker_loss} واحد ارتش "
                f"از بین رفت."
            )

        self.update_info()

        self.draw_map()

        self.check_victory()

    # =====================================================
    # NEIGHBOR
    # =====================================================

    def are_neighbors(
        self,
        a,
        b
    ):

        ax, ay = a.center()

        bx, by = b.center()

        distance = math.sqrt(
            (ax - bx) ** 2
            + (ay - by) ** 2
        )

        return distance <= 300

    # =====================================================
    # AI TURN
    # =====================================================

    def ai_turn(self):

        if self.player is None:
            return

        for ai in self.countries.values():

            if ai == self.player:
                continue

            if ai.owner != ai.name:
                continue

            # -------------------------
            # AI builds army
            # -------------------------

            if (
                ai.manpower >= 5
                and
                ai.rifles >= 20
            ):

                if random.random() < 0.35:

                    ai.manpower -= 5
                    ai.rifles -= 20
                    ai.army += 2

            # -------------------------
            # AI attack
            # -------------------------

            if random.random() > 0.10:
                continue

            targets = []

            for target in self.countries.values():

                if target == ai:
                    continue

                if target.owner == ai.name:
                    continue

                if self.are_neighbors(
                    ai,
                    target
                ):

                    targets.append(
                        target
                    )

            if not targets:
                continue

            target = random.choice(
                targets
            )

            if ai.army < target.army:
                continue

            ai_power = (
                ai.army
                * (1 + ai.infantry_tech * 0.1)
                * random.uniform(
                    0.7,
                    1.3
                )
            )

            target_power = (
                target.army
                * (1 + target.infantry_tech * 0.1)
                * random.uniform(
                    0.7,
                    1.2
                )
            )

            if ai_power > target_power:

                target.army -= random.randint(
                    2,
                    5
                )

                if target.army <= 0:

                    target.army = 1

                    target.owner = ai.name

                    self.log_message(
                        f"🤖 {ai.name} "
                        f"{target.name} را فتح کرد."
                    )

            else:

                ai.army = max(
                    1,
                    ai.army - random.randint(
                        1,
                        3
                    )
                )

    # =====================================================
    # VICTORY
    # =====================================================

    def check_victory(self):

        if self.player is None:
            return

        controlled = 0

        for country in self.countries.values():

            if country.owner == self.player.name:

                controlled += 1

        if controlled >= 4:

            self.game_over = True

            messagebox.showinfo(
                "🏆 پیروزی",
                f"تبریک!\n\n"
                f"{self.player.name} "
                f"بر اروپا مسلط شد!\n\n"
                f"مناطق تحت کنترل: "
                f"{controlled}"
            )

    # =====================================================
    # LOG
    # =====================================================

    def log_message(
        self,
        message
    ):

        self.log.insert(
            tk.END,
            message + "\n"
        )

        self.log.see(
            tk.END
        )


# =========================================================
# START GAME
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    game = MiniHOI(root)

    root.mainloop()
