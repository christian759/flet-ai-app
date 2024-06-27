import flet as ft
from flet_core import View
import enchant

# Declare tab_number as a global variable
tab_number = 1

def main(page: ft.Page):
    page.title = "Assiste"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 650
    page.window_height = 600

    def open_drawer(_):
        page.update()

    def tab_1operator(e: ft.RouteChangeEvent):
        page.route = '/assiste_ai/tab_1'
        page.go(page.route)
        page.update()

    def tab_operator(tab_no):
        page.route = f'/assiste_ai/{tab_no}'
        page.go(page.route)
        page.update()

    tab_row = ft.Row(
        width=page.window_width,
        scroll=ft.ScrollMode.ADAPTIVE,
        controls=[ft.Card(
            content=ft.Container(
                content=ft.ElevatedButton(
                    content=ft.Text(value="Tab 1", 
                                    size=15, 
                                    color=ft.colors.TEAL, 
                                    font_family="Trebuchet MS",
                                    selectable=True, 
                                    weight=ft.FontWeight.W_100
                    ),
                    on_click = tab_1operator,
                )
            )
        )]
    )

    def add_tab(_):
        global tab_number   
        tab_number += 1        
        tab_row.controls.append(
            ft.Card(
                content=ft.Container(
                    content=ft.ElevatedButton(
                        content=ft.Text(value=f"Tab {tab_number}", 
                                    size=13, 
                                    color=ft.colors.TEAL, 
                                    font_family="Trebuchet MS",
                                    selectable=True, 
                                    weight=ft.FontWeight.W_100
                        ),
                        on_click = tab_operator,
                    )
                )
            )
        )
        page.views.append(
            View(
                route=f'/assiste_ai/tab_{tab_number}',
                controls=[
                    ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Row(
                                        controls=[
                                            ft.IconButton(
                                                icon=ft.icons.ARROW_BACK_ROUNDED,
                                                on_click=view_pop
                                            ),
                                            ft.Text(value="Assiste AI", size=23, color=ft.colors.TEAL,
                                                    font_family="Trebuchet MS",
                                                    selectable=True, weight=ft.FontWeight.BOLD
                                            )
                                        ]
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            ft.IconButton(icon=ft.icons.ADD_ROUNDED, on_click=add_tab),
                                            ft.IconButton(icon=ft.icons.MORE_VERT, on_click=open_drawer),
                                        ]
                                    ),
                                ]
                            ),
                            ft.Divider(),
                            tab_row,
                            ft.Column(
                                height=page.window_height - 143,
                                scroll=ft.ScrollMode.ADAPTIVE,
                                controls=[
                                    ft.Card(
                                        content=ft.Container(
                                            content=another
                                        )
                                    ),
                                    ft.Row(
                                        alignment=ft.MainAxisAlignment.END,
                                        spacing=5,
                                        controls=[
                                            chat_box,
                                            ft.IconButton(autofocus=True, icon=ft.icons.SEND_ROUNDED, on_click=send,
                                                        bgcolor=ft.colors.TEAL_700, disabled_color=ft.colors.TEAL_500)
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        )
        page.update()

    try:
        from meta_ai_api import MetaAI
        ai = MetaAI()
        def open_assiste_ai(_):
            page.views.append(
                View(
                    route='/assiste_ai/tab_1',
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.IconButton(
                                                    icon=ft.icons.ARROW_BACK_ROUNDED,
                                                    on_click=view_pop
                                                ),
                                                ft.Text(value="Assiste AI", size=23, color=ft.colors.TEAL,
                                                        font_family="Trebuchet MS",
                                                        selectable=True, weight=ft.FontWeight.BOLD
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.IconButton(icon=ft.icons.ADD_ROUNDED, on_click=add_tab),
                                                ft.IconButton(icon=ft.icons.MORE_VERT, on_click=open_drawer),
                                            ]
                                        ),
                                    ]
                                ),
                                ft.Divider(),
                                tab_row,
                                ft.Column(
                                    height=page.window_height - 143,
                                    scroll=ft.ScrollMode.ADAPTIVE,
                                    controls=[
                                        ft.Card(
                                            content=ft.Container(
                                                content=another
                                            )
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            spacing=5,
                                            controls=[
                                                chat_box,
                                                ft.IconButton(autofocus=True, icon=ft.icons.SEND_ROUNDED, on_click=send,
                                                            bgcolor=ft.colors.TEAL_700, disabled_color=ft.colors.TEAL_500)
                                            ]
                                        )
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
            page.update()

        entry_message = ai.prompt(message="Hello")
        message1 = entry_message["message"]
        if "Meta" in message1:
            message1.replace("Meta", "Assiste")
        another = ft.Column(
                    run_spacing=10,
                    tight=False,
                    controls=[
                        ft.ListTile(
                            icon_color=ft.colors.TEAL_700,
                            leading=ft.Icon(ft.icons.WECHAT),
                            title=ft.Text("Assiste AI", weight=ft.FontWeight.BOLD),
                        ),
                        ft.Row(
                            wrap=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text(value=message1, font_family="Trebuchet MS",
                                                size=14, selectable=True,)
                                    ]
                                )
                            ]
                        )
                    ]
                )
    except:
        pass

    #d = enchant.Dict("en_US")
    def on_chatbox_change(_):
        if len(chat_box.value) >= 2: # and d.check(chat_box.value):
            chat_box.error_text = ""
        page.update()

    def send(_):
        aie = chat_box.value
        if len(chat_box.value) >= 2:
            another.controls.append(
                ft.Divider(thickness=1, height=2, color=ft.colors.TEAL_700)
            )
            page.update()
            another.controls.append(
                ft.Column(
                    controls=[
                        ft.ListTile(
                            icon_color=ft.colors.TEAL_700,
                            leading=ft.Icon(ft.icons.ACCOUNT_CIRCLE_ROUNDED),
                            title=ft.Text("You", weight=ft.FontWeight.BOLD),
                        ),
                        ft.Row(
                            wrap=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text(value=chat_box.value, font_family="Trebuchet MS",
                                                size=14, selectable=True,)
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
            chat_box.value = ""
            page.update()
            response = aie
            entry_message2 = ai.prompt(message=response)
            message2 = entry_message2["message"]
            page.update()
            another.controls.append(
                ft.Divider(thickness=1, height=2, color=ft.colors.TEAL_700)
            )
            another.controls.append(
                ft.Column(
                    controls=[
                        ft.ListTile(
                            icon_color=ft.colors.TEAL_700,
                            leading=ft.Icon(ft.icons.WECHAT),
                            title=ft.Text("Assiste AI", weight=ft.FontWeight.BOLD),
                        ),
                        ft.Row(
                            wrap=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text(value=message2, font_family="Trebuchet MS",
                                                size=14, selectable=True,)
                                    ]
                                )
                            ]
                        )
                    ]
                )
            )
            page.update()
        else:
            chat_box.error_text = "Please, Enter a Valid Message"
        page.update()


    def route_change(e: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(
            View(
                route='/',
                controls=[pg]
            )
        )
        if page.route == '/assiste_ai/tab_1':
            open_assiste_ai("_")
        if page.route == '/assiste_ai/tab_2':
            add_tab("-")
        if page.route == '/assiste_ai/tab_3':
            page.add(ft.AlertDialog(
                title="Premium"
            ))
        page.update()

    def view_pop(e: ft.ViewPopEvent):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    chat_box = ft.TextField(value="", hint_text="Message Here", text_align=ft.MainAxisAlignment.END,
                            border_radius=25, multiline=True, max_lines=6, width=250, border_color=ft.colors.TEAL_700,
                            autofocus=True, hover_color=ft.colors.BLACK26, capitalization=ft.TextCapitalization.SENTENCES,
                            on_change=on_chatbox_change, cursor_radius=40, cursor_width=3)
    search = ft.IconButton(icon=ft.icons.SEARCH, on_click=print("Hello"))
    icons = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    search,
                    ft.IconButton(icon=ft.icons.MORE_VERT, on_click=open_drawer)
                ]
            )
    heading_text = ft.Text(value="Welcome to Assiste", size=23, color=ft.colors.TEAL, font_family="Trebuchet MS",
                    selectable=True, weight=ft.FontWeight.BOLD)
    heading = ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    heading_text,
                    icons
                ]
    )

    try:
        assiste_ai_launcher = ft.Row(
            controls=[ft.TextButton("Open", on_click=open_assiste_ai)],
            alignment=ft.MainAxisAlignment.END,
        )
    except:
        assiste_ai_launcher = ft.Row(
            wrap=True,
            controls=[
                ft.Column(
                    spacing=50,
                    controls=[
                        ft.Text(value= "Assiste AI wasn't able to load, because there's no internet, \n Please, Check your Internet Connection and Try again later, \n  Thank you.", 
                                size=13, selectable=True, opacity=3,)
                    ]
                )
            ]
        )
        pass

    body = ft.Column(
                height=page.window_height - 143,
                scroll=ft.ScrollMode.ADAPTIVE,
                controls=[
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.ListTile(
                                        icon_color=ft.colors.TEAL_700,
                                        leading=ft.Icon(ft.icons.WECHAT),
                                        title=ft.Text("Assiste AI", weight=ft.FontWeight.BOLD),
                                        subtitle=ft.Text(
                                            "An AI Interactive ChatBot that can be informative, and good in answering questions."
                                        ),
                                    ),
                                    assiste_ai_launcher
                                ]
                            ),
                            padding=10,
                        )
                    ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.ListTile(
                                        icon_color=ft.colors.TEAL_700,
                                        leading=ft.Icon(ft.icons.CREATE_ROUNDED),
                                        title=ft.Text("Tools", weight=ft.FontWeight.BOLD),
                                    ),
                                    ft.Row(
                                        controls=[ft.TextButton("Calculator"), ft.TextButton("Calendar"),
                                                ft.TextButton("Notepad")],
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    ),
                                ]
                            ),
                            padding=10,
                        )
                    ),
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column(
                                controls=[
                                    ft.ListTile(
                                        icon_color=ft.colors.TEAL_700,
                                        leading=ft.Icon(ft.icons.LOCAL_MOVIES_ROUNDED),
                                        title=ft.Text("Entertainment", weight=ft.FontWeight.BOLD),
                                        subtitle=ft.Text(
                                            "Unlock a world of endless entertainment at your fingertips! \n Get ready to be entertained like never before, by games and movies"
                                        ),
                                    ),
                                    ft.Row(
                                        controls=[ft.TextButton("Open")],
                                        alignment=ft.MainAxisAlignment.END,
                                    ),
                                ]
                            ),
                            padding=10,
                        )
                    ),
                ]
            )
    pg = ft.Column(
            tight=True,
            auto_scroll=True,
            controls=[
                heading,
                ft.Divider(),
                body
            ]
        )
    if page.route == '/':
        route_change("e")
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.route = '/'
    page.go(page.route)


ft.app(target=main)
