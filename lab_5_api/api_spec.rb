require 'json'
require 'faraday'
require 'net/http'

BASE_URL = 'https://goweather.herokuapp.com/weather/'.freeze
RESPONSE_KEYS = %w[temperature wind description forecast].freeze

describe 'weather-api' do

  describe 'gdansk' do
    url = "#{BASE_URL}gdansk"
    response = Faraday.get url
    response_json = JSON.parse(response.body)

    it 'response status should be equal to 200' do
      expect(response.status).to eq 200
    end

    it 'response should contain certain keys' do
      expect(response_json.keys).to eq RESPONSE_KEYS
    end
  end

  describe 'thiscitydoesntexist' do
    url = "#{BASE_URL}thiscitydoesntexist"
    response = Faraday.get url
    response_json = JSON.parse(response.body)

    it 'response status should still be 200' do
      expect(response.status).to eq 200
    end

    it 'response should still contain those keys' do
      expect(response_json.keys).to eq RESPONSE_KEYS
    end

    it 'response temperature should be empty' do
      expect(response_json['temperature']).to be_empty
    end
  end
end
