const input_name = document.querySelector(".feedback #name");
const input_email = document.querySelector(".feedback #email");
const input_subject = document.querySelector(".feedback #subject");
const input_message = document.querySelector(".feedback #message");
const submit_button = document.querySelector(".feedback #submit_button");

const handlePost = async (data) => {
  await fetch(
    "https://shaxruxportfoliobackend.pythonanywhere.com/api/feedback/",
    {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    }
  )
    .then((res) => {
      console.log(res);
      input_name.value = "";
      input_email.value = "";
      input_subject.value = "";
      input_message.value = "";
    })
    .catch((err) => console.log(err));
};

submit_button.addEventListener("click", () => {
  const state = {
    name: input_name.value,
    email: input_email.value,
    subject: input_subject.value,
    message: input_message.value,
  };
  handlePost(state);
});
