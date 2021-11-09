from flask_appbuilder.widgets import RenderTemplateWidget

class AirflowModelListWidget(RenderTemplateWidget):
    template: str

class AirflowDateTimePickerWidget:
    data_template: str
    def __call__(self, field, **kwargs): ...
