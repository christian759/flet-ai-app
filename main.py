import flet as ft
from flet_core import View
import enchant
import openai
openai.api_key = "sk-proj-LiBI8BLzGqX0eBno4gfaT3BlbkFJu2qD3r1M2KB0Rmc1MTTe"


def main(page: ft.Page):
    page.title = "Assiste"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.window_width = 650
    page.window_height = 600

    def open_drawer(_):
        page.update()

    def chat_with_gpt(prompt):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content

    def open_assiste_ai(_):
        page.views.append(
            View(
                route='/assiste_ai',
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
                                            ft.IconButton(icon=ft.icons.ADD_ROUNDED, on_click=open_drawer),
                                            ft.IconButton(icon=ft.icons.MORE_VERT, on_click=open_drawer),
                                        ]
                                    ),
                                ]
                            ),
                            ft.Divider(),
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
                                    ft.Text(value=chat_with_gpt(chat_with_gpt("Hello")), font_family="Trebuchet MS",
                                            size=14, selectable=True,)
                                ]
                            )
                        ]
                    )
                ]
            )

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
            response = chat_with_gpt(aie)
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
                            # leading_and_trailing_text_style=ft.TextStyle,
                            title=ft.Text("Assiste AI", weight=ft.FontWeight.BOLD),
                        ),
                        ft.Row(
                            wrap=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Text(value=chat_with_gpt(response), font_family="Trebuchet MS",
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
        if page.route == '/assiste_ai':
            open_assiste_ai()
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
                                    ft.Row(
                                        controls=[ft.TextButton("Open", on_click=open_assiste_ai)],
                                        alignment=ft.MainAxisAlignment.END,
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
        route_change('hello')
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.route = '/'
    page.go(page.route)


ft.app(target=main)
