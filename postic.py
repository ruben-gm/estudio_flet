import flet as ft


def main(page: ft.Page):
    page.title = "ayuda mental"
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.padding = 17
    page.theme_mode = "light"
    
    def agregar_nota(e):
        new_nota = crear_nota("Nueva nota")
        grid.controls.append(new_nota)
        page.update()
    
    def borrar_nota(nota):
        grid.controls.remove(nota)
        page.update()
    
    
    def crear_nota(text):
        nota_content = ft.TextField(value=text, multiline=True,
                                    bgcolor=ft.colors.BLUE_GREY_50)
        nota = ft.Container(
            content=ft.Column([nota_content, ft.IconButton(icon=ft.icons.DELETE,
                                                               on_click=lambda _:borrar_nota(nota))]),
        width=200,
        height=200,
        bgcolor=ft.colors.BLUE_GREY_100,
        border_radius=10,
        padding=10    
        )
        return nota
        
    
#    nota = crear_nota("Mi primer postic")
#    nota_2 = crear_nota("Mi segunda nota")
#    page.add(nota, nota_2)

    grid = ft.GridView(
        expand=True,
        max_extent=200,
        child_aspect_ratio=1,
        spacing=20,
        run_spacing=20
#        horizontal=True
    )

    notas = [
       "Ir al gym",
        "IR a la escuelita",
        "Tomar awuita"
        
    ]
#    page.add(ft.Row(notas))
    for nota in notas:
        grid.controls.append(crear_nota(nota))
        
    page.add(
        ft.Row([
        ft.Text("Mis posticks adhesivos", size=22, weight="bold",
                color= ft.colors.WHITE),
        ft.IconButton(icon=ft.icons.ADD, on_click=agregar_nota, icon_color=ft.colors.WHITE)
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN), grid 
    )
    
    
ft.app(target=main) 
