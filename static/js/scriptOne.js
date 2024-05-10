function adicionarCampos() {
    var inputsContainer = document.getElementById('inputsContainer');
    var novaLinha = document.createElement('div');
    novaLinha.classList.add('row', 'mb-3');
    novaLinha.innerHTML = `
        <div class="col">
            <input type="text" class="form-control" name="peca" placeholder="Peca">
        </div>
        <div class="col">
            <input type="text" class="form-control" name="cor" placeholder="Cor">
        </div>
        <div class="col">
            <input type="number" class="form-control" name="qtd" placeholder="quantidade">
        </div>
    `;
    inputsContainer.appendChild(novaLinha);
}