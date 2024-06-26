from sqladmin import ModelView, Admin

from src.v1.admins.pictures.forms import CreateCapitalCityAdminForm
# from src.v1.pictures.models import Picture


# class CapitalCityAdmin(ModelView, model=Picture):
#     """- представление название городов """
#
#     form = CreateCapitalCityAdminForm
#     column_labels = {Picture.city: "Города", Picture.country: "Страна",
#                      Picture.updated_date: "Дата обновления", Picture.created_date: "Дата создания",
#                      "longitude": "Долгота", "latitude": "Широта",}
#     name = "Столицы городов"
#     name_plural = "Столицы городов"
#     category = "Города"
#     column_list = [Picture.id, Picture.country, Picture.city, 'longitude', 'latitude',
#                    Picture.created_date, Picture.updated_date]
#     column_details_list = [Picture.country, Picture.city, 'longitude', 'latitude',
#                            Picture.created_date, Picture.updated_date, ]
#
#     async def on_model_change(self, data, model, is_created, request):
#         """- переопределить метод при создании данных """
#         if is_created is True:
#             longitude = data.pop('longitude')
#             latitude = data.pop('latitude')
#
#
# async def register_views(app_admin: Admin) -> Admin:
#     """- инициализация представления админ панели """
#     app_admin.add_view(CapitalCityAdmin)
#     return app_admin

