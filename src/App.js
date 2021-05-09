import './App.css';
import React, { Component } from 'react';
import logo from './template.png'
import axios from 'axios';

class App extends Component {
  constructor() {
    super()
    this.state = {
      previewImage: logo,
      email: '',
      password: '',
      emailSubject: '',
      emailBody: '',
      xCoordinate: 0,
      yCoordinate: 0,
      imageName: 'certificateImage.png'
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleTextChange = this.handleTextChange.bind(this)
  }

  handleChange(e) {
    this.setState({
      [e.target.name]: e.target.files[0]
    })
    if(e.target.name === 'certificateImage') {
      console.log(e.target.files[0])
      this.setState({
        imageName : e.target.files[0].name,
        previewImage: URL.createObjectURL(e.target.files[0])
      })
    }
  }

  handleTextChange(e) {
    this.setState({
      [e.target.name]: e.target.value
    })
  }

  handleSubmit(e) {
    const fileData = new FormData()
    fileData.append('certificateImage', this.state.certificateImage)
    fileData.append('certificateFont', this.state.certificateFont)
    fileData.append('certificateCSV', this.state.certificateCSV)
    const textData = new FormData()
    textData.append('email', this.state.email)
    textData.append('password', this.state.password)
    textData.append('emailSubject', this.state.emailSubject)
    textData.append('emailBody', this.state.emailBody)
    textData.append('xCoordinate', this.state.xCoordinate)
    textData.append('yCoordinate', this.state.yCoordinate)
    textData.append('imageName', this.state.imageName)
    axios.post("https://cert-gen.herokuapp.com/upload", fileData)
    .then(res => {
      console.log(res.statusText);
    })
    axios.post("https://cert-gen.herokuapp.com/python", textData)
    .then(res => {
      console.log(res.data);
    })
  }

  render() {
    return (
      <div className="App">
        <div className="App-heading">
          <h1 id="title">DSC KIIT Certificate Generator</h1>
        </div>
        <div className="App-content">
          <div className="form-container">
            <form>
              <label className="form-label">Email</label>
              <input type="text" id="email" name="email" placeholder="johndoe@gmail.com" onChange={this.handleTextChange}/>
              <label className="form-label">Password</label>
              <input type="password" id="password" name="password" placeholder="password" onChange={this.handleTextChange}/>
              <label className="form-label">Certificate Image</label>
              <input type="file" id="certificate-image" name="certificateImage" onChange={this.handleChange}/>
              <label className="form-label">Font</label>
              <input type="file" id="certificate-font" name="certificateFont" onChange={this.handleChange}/>
              <label className="form-label">CSV</label>
              <input type="file" id="certificate-csv" name="certificateCSV" onChange={this.handleChange}/>
              <label className="form-label">Coordinates (x,y)</label>
              <div className="form-coordinates">
                <input type="text" className="coordinates" id="x-coordinate" name="xCoordinate" placeholder="990" onChange={this.handleTextChange}/>
                <input type="text" className="coordinates" id="y-coordinate" name="yCoordinate" placeholder="680" onChange={this.handleTextChange}/>
              </div>
              <label className="form-label">Subject</label>
              <input type="text" id="email-subject" name="emailSubject" placeholder="Certificate of Participation" onChange={this.handleTextChange}/>
              <label className="form-label">Body</label>
              <textarea id="email-body" name="emailBody" placeholder="Hey, Thank you for participating in our event attached below is the certificate of your Partiicipation" rows={5} cols={30} onChange={this.handleTextChange}/>
              <button type='button' className="btn-submit" onClick={this.handleSubmit}>Submit</button>
            </form>
          </div>
          <div className="image-preview">
            <img src={this.state.previewImage} alt="logo" width="100%"></img>
          </div>
        </div>
      </div>
    )
  }
}

export default App;
