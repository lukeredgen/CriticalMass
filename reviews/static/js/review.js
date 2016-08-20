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

var Review = React.createClass({
    getInitialState: function() {
        return {
            name: ''
        };
    },
  componentDidMount: function() {
    this.serverRequest = $.get(this.props.source, function (result) {
      var review = result[0];
      this.setState({
        name: review.name
      });
    }.bind(this));
  },
    componentWillUnmount: function () {
        this.serverRequest.abort();
    },
    render: function () {
        return (
            <div>
                <h2>{this.state.name}</h2>
            </div>
        )
    }
});

ReactDOM.render(
    <Review source="http://localhost:8000/reviews/api/albums/1" />,
    document.getElementById('content')
)