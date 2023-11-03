$(document).ready(function() {
    $('a[data-confirm]').click(function(ev){
        var href = $(this).attr('href');
        if(!$('#realizar-logout').lenght){
            $('body').append('<div class="modal fade" id="realizar-logout" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"><div class="modal-dialog"><div class="modal-content"><div class="modal-header bg-danger text-white">REALIZAR LOGOUT NO SISTEMA<button type="button" class="btn-close" data-dismiss="modal" aria-label="Close"></button></div><div class="modal-body">Tem certeza que deseja sair do sistema?</div><div class="modal-footer"><button type="button" class="btn btn-primary" data-dismiss="modal">Cancelar</button><a class="btn btn-danger text-white" id="dataConfirmOK">Sair/Logout</a></div></div></div></div>');
        }
        $('#dataConfirmOK').attr('href', href);
        $('#realizar-logout').modal({show:true});
        return false;
    });
});