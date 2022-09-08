import { GraphQLClient, gql } from 'graphql-request'

// authorization token that lets us query from rate my professor's website
const AUTH_TOKEN = 'dGVzdDp0ZXN0'
// url where we access the query
const WEB_URL = 'https://www.ratemyprofessors.com/graphql'
// client object where the url and authorization token are combined
const graphQLClient = new GraphQLClient(WEB_URL, {
  headers: {
    authorization: `Basic ${AUTH_TOKEN}`
  }
})
// query in which data is returned
const test_query = gql`
query NewSearchSchoolsQuery(query: 'cal poly pomona') {
    newSearch {
      schools(query: $query) {
        edges {
          cursor
          node {
            id
            legacyId
            name
            city
            state
          }
        }
        pageInfo {
          hasNextPage
          endCursor
        }
      }
    }
  }  
`
// creates the request with the query to the specified client
const data = graphQLClient.request(test_query)
// displays data 
data.then(function(result) {
    console.log(result)
})
