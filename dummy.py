# class CreateView:
#     def __init__(self, request, model, method, context={}):
#         self.request = request
#         self.model = model
#         self.method = method
#         self.context = context

#     def process(self):
#         self.context['data'] = self.model.objects.get(pk=1) if self.method == "get" else About.objects.all()

#     def render(self):
#         self.process()
#         return render(self.request, f'{self.model.__name__.lower()}.html', self.context)