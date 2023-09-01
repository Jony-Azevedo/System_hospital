$(document).ready(function() {
    $('#search').on('keyup', function() {
    var termo = $(this).val().toLowerCase();
    //loop para cada tr do corpo da tabela
    $('tbody tr').each(function() {
        var linha = $(this);
        var colunas = linha.find('td:nth-child(2), td:nth-child(6)');// Seleciona as colunas 2 (Nome) e 6 (E-mail)
        //loop para cada td das colunas nome e email
        colunas.each(function() {
        var coluna = $(this);
        var valorColuna = coluna.text().toLowerCase();
        if (valorColuna.includes(termo)) {
            linha.show();
                return false;
        } else {
                linha.hide();
            }
        });
    });
    });
});