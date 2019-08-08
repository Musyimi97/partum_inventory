from django.conf.urls import url, include

from pis_sales.views import (
    GenerateInvoiceAPIView, ProductItemAPIView, CreateInvoiceView,
    UpdateInvoiceView, InvoiceDetailView, UpdateInvoiceAPIView, InvoicesList,
    ProductDetailsAPIView, SalesDeleteView
)

urlpatterns = [
    url(
        r'^create/invoice/$',
        CreateInvoiceView.as_view(),
        name='create_invoice'
    ),
    url(
        r'^update/(?P<id>\d+)/api/$',
        UpdateInvoiceView.as_view(),
        name='invoice_update'
    ),
    url(
        r'^product/items/details/$',
        ProductItemAPIView.as_view(),
        name='product_item_api'
    ),
    url(
        r'^invoice/list/$',
        InvoicesList.as_view(),
        name='invoice_list'
    ),
    url(
        r'^api/generate/invoice/$',
        GenerateInvoiceAPIView.as_view(),
        name='generate_invoice_api'
    ),
    url(
        r'^api/update/invoice/$',
        UpdateInvoiceAPIView.as_view(),
        name='update_invoice_api'
    ),
    url(
        r'^invoice/(?P<invoice_id>\d+)/detail/$',
        InvoiceDetailView.as_view(),
        name='invoice_detail'
    ),
    url(
        r'^api/product/details/$',
        ProductDetailsAPIView.as_view(),
        name='product_details_api'
    ),
    url(
        r'^invoice/(?P<pk>\d+)/delete/$',
        SalesDeleteView.as_view(),
        name='delete'
    ),
]
