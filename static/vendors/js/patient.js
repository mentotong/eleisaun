// const alertBox = document.getElementById('alert-box')
// const imgBox = document.getElementById('img-box')
const form = document.getElementById('patient-create-form')
const first_name = document.getElementById('id_first_name')
const last_name = document.getElementById('id_last_name')
const sex = document.getElementById('id_sex')
const dob = document.getElementById('id_dob')
const profile_pic = document.getElementById('id_profile_pic')
const pob = document.getElementById('id_pob')
const blood_type = document.getElementById('id_blood_type')
const occupation = document.getElementById('id_occupation')
const address = document.getElementById('id_address')
const bairu = document.getElementById('id_bairu')
const suku = document.getElementById('id_suku')
const postu = document.getElementById('id_postu')
const munisipiu = document.getElementById('id_munisipiu')
const mobile_1 = document.getElementById('id_mobile_1')
const mobile_2 = document.getElementById('id_mobile_2')
const mobile_3 = document.getElementById('id_mobile_3')
const email_1 = document.getElementById('id_email_1')
const email_2 = document.getElementById('id_email_2')
const kartaun_eleitoral = document.getElementById('id_kartaun_eleitoral')
const billete_identidade = document.getElementById('id_billete_identidade')
const pasaporte = document.getElementById('id_pasaporte')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
console.log(csrf)

const url = ""

// const handleAlerts = (type, text) =>{
//     alertBox.innerHTML = `<div class="alert alert-${type}" role="alert">
//                             ${text}
//                         </div>`
// }

// image.addEventListener('change', ()=>{
//     const img_data = image.files[0]
//     const url = URL.createObjectURL(img_data)
//     console.log(url)
//     imgBox.innerHTML = `<img src="${url}" width="100%">`
// })

form.addEventListener('submit', event=>{
    event.preventDefault()
    console.log(url)

    const form_data = new FormData()
    form_data.append('csrfmiddlewaretoken', csrf[0].value)
    form_data.append('first_name', first_name.value)
    form_data.append('last_name', last_name.value)
    form_data.append('sex', sex.value)
    form_data.append('dob', dob.value)
    form_data.append('profile_pic', profile_pic.files[0])
    form_data.append('pob', pob.value)
    form_data.append('blood_type', blood_type.value)
    form_data.append('occupation', occupation.value)
    form_data.append('address', address.value)
    form_data.append('bairu', bairu.value)
    form_data.append('suku', suku.value)
    form_data.append('postu', postu.value)
    form_data.append('munisipiu', munisipiu.value)
    form_data.append('mobile_1', mobile_1.value)
    form_data.append('mobile_2', mobile_2.value)
    form_data.append('mobile_3', mobile_3.value)
    form_data.append('email_1', email_1.value)
    form_data.append('email_2', email_2.value)
    form_data.append('kartaun_eleitoral', kartaun_eleitoral.value)
    form_data.append('billete_identidade', billete_identidade.value)
    form_data.append('pasaporte', pasaporte.value)

    $.ajax({
        type: 'POST',
        url: url,
        headers: {
            "X-Requested-With": "XMLHttpRequest",
          },
        enctype: 'multipart/form-data',
        data: form_data,
        success: function(response){
            console.log(response)
            // const sText = `successfully saved ${response.name}`
            // handleAlerts('success', sText)
            // setTimeout(()=>{
            //     alertBox.innerHTML = ""
            //     imgBox.innerHTML = ""
            //     name.value = ""
            //     description.value = ""
            //     image.value = ""
            // }, 3000)
        },
        error: function(error){
            console.log(error)
            // handleAlerts('danger', 'ups..something went wrong')
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})

console.log(form)