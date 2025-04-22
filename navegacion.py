import flet as ft

def main(page: ft.Page):
    # Configuración inicial de la página
    page.title = "ejemplo de navegacion"
    page.bgcolor = ft.colors.BLUE_GREY_100
    
    titulo = ft.Text("Ejemplo de navigationBar")
    
    def boton_elemento_navegacion(e):
        """Maneja la navegación entre diferentes páginas"""
        seleccion_index = e.control.selected_index
        if seleccion_index == 0:
            show_home()
        elif seleccion_index == 1:
            page.controls.clear()
            page.add(navigacion_bar, ft.Text("Página de búsqueda", size=30))
            page.update()
        elif seleccion_index == 2:
            page.controls.clear()
            page.add(navigacion_bar, ft.Text("Página de configuración", size=30))
            page.update()
        
    def show_home():
        """Muestra la página principal con el contador"""
        page.controls.clear()
        contador.value = f"Contador: {contador_valor}"
        page.add(navigacion_bar, contador, btn_increment, btn_decrement)
        page.update()
         
    contador = ft.Text("Contador: 0", size=30, color=ft.colors.WHITE)
    contador_valor = 0
    
    def increment_contador(e):
        """Incrementa el valor del contador"""
        nonlocal contador_valor
        contador_valor += 1
        contador.value = f"Contador: {contador_valor}"
        page.update()
        
    def decrement_contador(e):
        """Decrementa el valor del contador"""
        nonlocal contador_valor
        contador_valor -= 1
        contador.value = f"Contador: {contador_valor}"
        page.update()        
    
    btn_increment = ft.ElevatedButton("Increment", on_click=increment_contador)
    btn_decrement = ft.ElevatedButton("Decrement", on_click=decrement_contador)    
    
    # Barra de navegación con tres destinos
    navigacion_bar = ft.NavigationBar(
        selected_index=0,
        on_change=boton_elemento_navegacion,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.icons.SEARCH, label="Search"),
            ft.NavigationBarDestination(icon=ft.icons.SETTINGS, label="Settings")                        
        ],
        bgcolor=ft.colors.AMBER_400,
        indicator_color=ft.colors.RED_ACCENT_100
    )
    
    page.add(navigacion_bar)
    show_home()

# Iniciar la aplicación
if __name__ == "__main__":
    ft.app(target=main)