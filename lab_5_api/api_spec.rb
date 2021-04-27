require 'json'
require 'faraday'
require 'net/http'

BASE_URL = 'https://goweather.herokuapp.com/weather/'.freeze
RESPONSE_KEYS = %w[temperature wind description forecast].freeze

describe 'when you request weather forecast from weather-api' do
  let(:response) { Faraday.get url }
  let(:response_json) { JSON.parse(response.body) }

  context 'when you include real city' do
    let(:url) { "#{BASE_URL}gdansk" }

    it 'has a response status equal to 200' do
      expect(response.status).to eq 200
    end

    it 'has a response containing certain keys' do
      expect(response_json.keys).to match_array RESPONSE_KEYS
    end
  end

  context 'when you include city that does not exist' do
    let(:url) { "#{BASE_URL}thiscitydoesntexist" }

    it 'responses with 200 status' do
      expect(response.status).to eq 200
    end

    it 'responses with certain keys' do
      expect(response_json.keys).to match_array RESPONSE_KEYS
    end

    it 'responses with empty temperature' do
      expect(response_json['temperature']).to be_empty
    end
  end

  context 'when you do not include any city' do
    let(:url) { BASE_URL }

    it 'responses with 404 status' do
      expect(response.status).to eq 404
    end
  end
end
