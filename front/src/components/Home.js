import pic1 from "../resources/pic1.png";
import pic2 from "../resources/pic2.png";
import pic3 from "../resources/pic3.png";

const Home = () => {
  return (
    <div className={"home-container"}>
      <div className={"home-carousel"}>
        <div
          id="carouselExampleCaptions"
          className="carousel slide"
          data-bs-ride="false"
        >
          <div className="carousel-indicators">
            <button
              type="button"
              data-bs-target="#carouselExampleCaptions"
              data-bs-slide-to="0"
              className="active"
              aria-current="true"
              aria-label="Slide 1"
            ></button>
            <button
              type="button"
              data-bs-target="#carouselExampleCaptions"
              data-bs-slide-to="1"
              aria-label="Slide 2"
            ></button>
            <button
              type="button"
              data-bs-target="#carouselExampleCaptions"
              data-bs-slide-to="2"
              aria-label="Slide 3"
            ></button>
          </div>
          <div className="carousel-inner" style={{ borderRadius: "20px" }}>
            <div className="carousel-item active">
              <img src={pic1} className="d-block w-100" alt="..." />
              <div className="carousel-caption d-none d-md-block">
                <h5>Analyse thousands reviews in a click of a button</h5>
              </div>
            </div>
            <div className="carousel-item" data-bs-interval="5000">
              <img src={pic2} className="d-block w-100" alt="..." />
              <div className="carousel-caption d-none d-md-block">
                <h5>See your customers needs</h5>
              </div>
            </div>
            <div className="carousel-item" data-bs-interval="5000">
              <img src={pic3} className="d-block w-100" alt="..." />
              <div className="carousel-caption d-none d-md-block">
                <h5>Improve experience</h5>
              </div>
            </div>
          </div>
          <button
            className="carousel-control-prev"
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide="prev"
          >
            <span
              className="carousel-control-prev-icon"
              aria-hidden="true"
            ></span>
            <span className="visually-hidden">Previous</span>
          </button>
          <button
            className="carousel-control-next"
            type="button"
            data-bs-target="#carouselExampleCaptions"
            data-bs-slide="next"
          >
            <span
              className="carousel-control-next-icon"
              aria-hidden="true"
            ></span>
            <span className="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;
