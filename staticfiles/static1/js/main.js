(function($) {
    "use strict";


    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input3').each(function() {
        $(this).on('blur', function() {
            if ($(this).val().trim() != "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        })
    })


    /*==================================================================
    [ Chose Radio ]*/
    $("#radio1").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideUp(300);
        }
    });

    $("#radio2").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideDown(300);
        }
    });

    $("#radio3").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideUp(300);
        }
    });

    $("#radio4").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideDown(300);
        }
    });

    $("#radio5").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideUp(300);
        }
    });

    $("#radio6").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideDown(300);
        }
    });

    $("#radio7").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideUp(300);
        }
    });

    $("#radio8").on('change', function() {
        if ($(this).is(":checked")) {
            $('.input3-select').slideDown(300);
        }
    });


    /*==================================================================
    [ Validate ]*/
    var name = $('.validate-input input[name="name"]');


    $('.validate-form').on('submit', function() {
        var check = true;

        if ($(name).val().trim() == '') {
            showValidate(name);
            check = false;
        }



        return check;
    });


    $('.validate-form .input3').each(function() {
        $(this).focus(function() {
            hideValidate(this);
        });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }



})(jQuery);