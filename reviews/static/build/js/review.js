/**
 * Created by Luke on 20/08/2016.
 */
// var ReviewComponent = React.createClass({
//     getInitialState: function () {
//
//     },
//     render: function () {
//         var testStyle = {fontSize: '18px', marginRight: '20px'};
//         return (
//             <div style={testStyle}>
//                 {this.props.reviews.map(function (review) {
//                     return (
//                         <Review name={review.name} release_date={review.release_date} image={review.cover_url}/>
//                     )
//                 })}
//             </div>
//         )
//     }
// });

var AddAlbumForm = React.createClass({
    render: function() {
        return(
            <div>
                <div>
                    <div>
                        <div>
                            <input type="text" placeholder="Title"/>
                        </div>
                        <div>
                            <input type="text" placeholder="Creator"/>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
});

var Review = React.createClass({
    getInitialState: function() {
        return {
            albums: []
        };
    },
  componentDidMount: function() {
    var _this = this;
    this.serverRequest =
      axios
        .get("http://localhost:8000/reviews/api/albums/")
        .then(function(result) {
          _this.setState({
            albums: result.data
          });
        })
  },
    // handleSubmit: function(data, e){
    //     var _this = this;
    //     this.serverRequest =
    //         axios
    //             .post("http://localhost:8000/reviews/api/albums/", {
    //                 name:
    //     })
    // },
    componentWillUnmount: function () {
        this.serverRequest.abort();
    },
    render: function () {
        return (
            <div>
                <h1>Albums</h1>
                {this.state.albums.map(function(album){
                    return (
                        <div key={album.id} className="album">
                            {album.name}
                            <br/>
                            <img src={album.cover_url}/>
                        </div>
                    );
                })}
            <AddAlbumForm/>
            </div>
        )
    }
});

ReactDOM.render(
    <Review />,
    document.getElementById('content')
)