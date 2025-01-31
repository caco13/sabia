const initMercadoPagoButton = function (pubKey, prevenceId) {
    const mp = new MercadoPago(pubKey, {
        locale: 'pt-BR'
    });

    mp.checkout({
        preference: {
            id: prevenceId
        },
        render: {
            container: '.cho-container',
            label: 'Fazer pagamento',
        }
    });
}

$("#mp_button").click(function (e) {
    e.preventDefault();
})