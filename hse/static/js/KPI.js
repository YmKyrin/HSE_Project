const formContainer = document.querySelector(".form-container");
        const nextBtn = document.querySelector(".nextBtn");
        const backBtn = document.querySelector(".backBtn");

        let currentPage = 0;

        nextBtn.addEventListener("click", () => {
            if (currentPage < 7) { // 0-based index for 11 pages
                currentPage++;
                formContainer.style.transform = `translateX(-${currentPage * 9.09}%)`;
            }
        });

        backBtn.addEventListener("click", () => {
            if (currentPage > 0) {
                currentPage--;
                formContainer.style.transform = `translateX(-${currentPage * 9.09}%)`;
            }
        })
