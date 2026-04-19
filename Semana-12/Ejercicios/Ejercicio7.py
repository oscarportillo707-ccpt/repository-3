montoCompra = float(input("Ingresa el monto de la compra: $"))

if montoCompra > 100:
    descuento = montoCompra * 0.20
    totalPagar = montoCompra - descuento
    print("Tienes un descuento del 20%. El total a pagar es: $", totalPagar)
elif montoCompra >= 50 and montoCompra <= 100:
    descuento = montoCompra * 0.10
    totalPagar = montoCompra - descuento
    print("Tienes un descuento del 10%. El total a pagar es: $", totalPagar)
elif montoCompra >= 0 and montoCompra < 50:
    print("No tienes descuento. El total a pagar es: $", montoCompra)
else:
    print("Monto de compra inválido.")
