import flet as ft

def main(page:ft.Page):
    page.bgcolor = ft.colors.BLUE_GREY_800
    page.title = "ayuda mental"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo = ft.Text(value="Lista de Tareas con FLet", 
                     size=30, weight=ft.FontWeight.BOLD)
    
    
    
    
    
    
    def agregar_tarea(e):
        if campo_tarea.value:
            tarea = ft.ListTile(title=ft.Text(campo_tarea.value),
                                leading=ft.Checkbox(on_change=seleccionar_tarea))
            tareas.append(tarea)
            campo_tarea.value = ""
            actualizar_tarea()

    def seleccionar_tarea(e):
        seleccionadas = [t.title.value for t in tareas if t.leading.value]
        tareas_seleccionadas.value = "Tareas seleccionadas: " + ", ".join(seleccionadas)
        page.update()
    
    def actualizar_tarea():
        lista_tareas.controls.clear()
        lista_tareas.controls.extend(tareas)
        page.update()
    
    
    campo_tarea = ft.TextField(hint_text="Escribe una nueva tarea")
    boton_agregar = ft.FilledButton(text="Agregar tarea", on_click = agregar_tarea)
    
    lista_tareas = ft.ListView(expand=1, spacing=3)
     
    
    
    
    tareas = []
    
    tareas_seleccionadas = ft.Text(value="", size=20, weight=ft.FontWeight.BOLD)
    
    page.add(titulo, campo_tarea, boton_agregar, lista_tareas, tareas_seleccionadas)
    
ft.app(target=main)    