import gql from 'graphql-tag'

export const QUERY_STACK = gql`
  query getStack($name: String!) {
    stack(name: $name) {
      name
      state
      networkMode
      odooVersion
      dbVersion
      servicesCount
      containers
    }
  }
`
export const QUERY_STACKS = gql`
  query getStacks {
    stacks {
      name
      state
    }
  }
`
