
const load_more_videos = (entries, observer) => {
    entries.forEach(element => {

        if (element.isIntersecting && loading!= true ) {
            // console.log("comence a cargar videos");

            loading = true;
            fetch_data().then((response)=>{
                loading = false;
                // console.log("termine de cargar videos");
            })
        }
    });
}

let page_token = "none";

let loading = false;




window.addEventListener('load', async () => {

    await fetch_data(1)
    await fetch_data(2)

    add_intersectionOberver();

})



const fetch_data = async (a) =>{

    const content = document.getElementById('content');
    const observer_target = document.getElementById('observer_target');

    let = new_page_tk = '';

    for (let i = 0; i < 4; i++) {
        element = create_video_container(`${i}`)

        content.insertBefore(element,observer_target)
    }

    await fetch(`/youtube_api_v3_video_data/${page_token}`).then((response)=>{
        return response.json()
    }).then((data)=>{
        page_token = data.nextPageToken
        let id = 0;
        data.items.forEach(element => {

            const ID = element.id;

            let thumbnail = document.getElementById(`thumbnail-image-${id}`)
            let video_url = document.getElementById(`video-url-${id}`)
            let channel_name = document.getElementById(`video-channel-name-${id}`)
            let video_title = document.getElementById(`video-title-${id}`)
            let timestamp = document.getElementById(`date-${id}`)

            thumbnail.src = element.snippet.thumbnails.standard.url;
            thumbnail.id = `thumbnail-image-${ID}`

            channel_name.innerText = element.snippet.channelTitle;
            channel_name.id = `video-channel-name-${ID}`

            video_title.innerText = element.snippet.title
            video_title.id = `video-title-${ID}`

            timestamp.innerText = new Date(element.snippet.publishedAt).toDateString()
            timestamp.id = `date-${ID}`

            video_url.href = `/watch_video/video_id=${ID}/channel=${element.snippet.channelTitle}`
            video_url.id = `video-url-${ID}`

            id++;
        });
    })

    console.log("termine desde el ftech");

}

const add_intersectionOberver = async ( ) =>{

    let options = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    }

    let observer = new IntersectionObserver(load_more_videos, options);
    let target = document.getElementById("observer_target")
    observer.observe(target)
}







const create_video_container = (id) => {

    let element = create_complex_element({
        name: 'article',
        class_name: 'video-container',
        id: 'video-container-' + id,
        childs: []
    })

    element.appendChild(create_video_header(id))
    element.appendChild(create_video_bottom_section(id))

    return element;
}

const create_video_header = (id, thumbnail_url = "https://media.tenor.com/i9mLzgx-690AAAAC/loading.gif") => {
    return create_complex_element({
        name: 'a',
        class_name: 'thumbnail',
        id: 'video-url-' + id,
        childs: [
            {
                name: 'img',
                class_name: 'thumbnail-image',
                id: 'thumbnail-image-' + id,
                attr: {
                    src: thumbnail_url
                },
                childs: []
            }

        ]
    })
}
const create_video_bottom_section = (id) => {
    return create_complex_element({
        name: 'div',
        class_name: 'video-bottom-section',
        id: 'video-details-' + id,
        childs: [
            {
                name: 'a',
                class_name: 'channel-id',
                id: 'channel-id' + id,
                childs: [
                    {
                        name: 'img',
                        class_name: 'channel-icon',
                        id: 'channel-icon-' + id,
                        attr: {
                            src: "https://cdn-icons-png.flaticon.com/512/149/149071.png"
                        },
                        childs: []
                    }
                ]
            },
            {
                name: 'div',
                class_name: 'video-details',
                id: 'video-details-' + id,
                childs: [
                    {
                        name: 'a',
                        class_name: 'video-title',
                        attr: {
                            innerText: "video title"
                        },
                        id: 'video-title-' + id,
                        childs: []
                    },
                    {
                        name: 'a',
                        class_name: 'video-channel-name',
                        id: 'video-channel-name-' + id,
                        attr: {
                            innerText: "channel_name"
                        },
                        childs: []
                    },

                    {
                        name: 'div',
                        class_name: 'video-metadata',
                        id: 'video-metadata-' + id,
                        childs: [
                            {
                                name: 'span',
                                class_name: 'views',
                                id: 'views-' + id,
                                attr: {
                                    innerText: "0"
                                },
                                childs: []
                            },

                            {
                                name: 'text',
                                class_name: 'text-',
                                id: 'text-' + id,
                                attr: {
                                    innerText: " • "
                                },
                                childs: []
                            },

                            

                            {
                                name: 'span',
                                class_name: 'date',
                                id: 'date-' + id,
                                attr: {
                                    innerText: "hoy"
                                },
                                childs: []
                            }]
                    },




                ]

            }



        ]
    }
    )
}

const create_complex_element = (element_details) => {

    const element = create_element(element_details.name, element_details.class_name, element_details.id);

    try {
        Object.keys(element_details.attr).forEach(attr => {
            element[`${attr}`] = element_details.attr[`${attr}`]
        });


    } catch {
    }

    if (element_details.childs.length) {

        element_details.childs.forEach(child => {
            element.appendChild(create_complex_element(child))
        });
    }


    return element;
}

const create_element = (type, clas_name = '', id = '') => {
    const element = document.createElement(type);
    element.classList.add(clas_name)
    element.id = id
    return element;
}
