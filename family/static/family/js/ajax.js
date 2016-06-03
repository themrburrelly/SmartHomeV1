function aj_toggle_switch(switch_id){
    $.ajax({
        type:"POST",
        url: "/family/aj_toggle_switch/",
        data:{'switch_id':switch_id,'csrfmiddlewaretoken': $("input[name=csrfmiddlewaretoken]").val()},
        dataType: 'text'
    });
};
