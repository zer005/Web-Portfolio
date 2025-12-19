const Home = () => {
  return (
    <div className="text-center py-12">
      <h1 className="text-4xl font-bold text-gray-900 mb-4">
        Welcome to My Portfolio
      </h1>
      <p className="text-lg text-gray-600">
        Full-stack portfolio website under construction
      </p>
      <div className="mt-8">
        <div className="inline-flex space-x-4">
          <button className="btn-primary">
            View Projects
          </button>
          <button className="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50">
            Contact Me
          </button>
        </div>
      </div>
    </div>
  );
};

export default Home;