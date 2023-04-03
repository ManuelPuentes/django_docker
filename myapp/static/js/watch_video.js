window.onload = () => {
    let url = window.location.href.split("/");
    let video_id = url[url.length-2];


    document.getElementById("add_comment").addEventListener('click',(e)=>{
        e.preventDefault();

        let comment = document.getElementById("comment");
        
        let value = comment.value;
        comment.value = ''


        console.log("estan creando un mensaje");
        console.log("tu comentario es ", value)

        console.log(document.cookie);

        if(value != ''){
            fetch(`/comment_video/${value}`, 
            {
                method:'POST', 
                csrftoken:document.cookie.csrftoken 
            }).then((response)=>{
                console.log(response);
            })
        }



    })





}







