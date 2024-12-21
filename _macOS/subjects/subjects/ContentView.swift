//
//  ContentView.swift
//  subjects
//
//  
//

import SwiftUI



struct ContentView: View
{
    var body: some View
    {
        VStack
        {
            // Text should be "Hello World!"
            Text("Hello World!")
        }
        .padding()
        
        
        
        .toolbar
        {
            ToolbarItem(placement: .navigation)
            { // Places the button on the left
                Button {
                    print("do something")
                } label: {
                    Text("Press Here")
                }
            }
        }
        
        
        
        
        
    }
}
