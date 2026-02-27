#!/bin/bash

# Função para realizar os cálculos
calcular() {
    echo "---------------------------"
    read -p "Digite o primeiro número: " num1
    read -p "Digite a operação (+, -, *, /): " oper
    read -p "Digite o segundo número: " num2
    echo "---------------------------"

    # 'bc -l' permite cálculos com decimais
    # 'scale=2' define duas casas decimais no resultado
    resultado=$(echo "scale=2; $num1 $oper $num2" | bc -l)

    echo "O resultado é: $resultado"
}

# Loop principal
while true; do
    echo "
    === CALCULADORA SHELL ===
    1. Calcular
    2. Sair
    "
    read -p "Escolha uma opção: " opcao

    case $opcao in
        1) calcular ;;
        2) echo "Saindo..."; exit 0 ;;
        *) echo "Opção inválida!" ;;
    esac
done