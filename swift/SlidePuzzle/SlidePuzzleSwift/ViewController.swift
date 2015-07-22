//
//  ViewController.swift
//  SlidePuzzleSwift
//
//  Created by Kentaro Wada on 10/22/14.
//  Copyright (c) 2014 Kentaro Wada. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    var pointOfBlank: CGPoint?
    var pieceViews: [UIImageView]?
    let kNumberOfRows = 4
    let kNumberOfColumns = 4
    let kNumberOfPieces = 4 * 4 - 1
    
    @IBOutlet weak var mainView: UIView!
    @IBOutlet weak var imageView: UIView!
    @IBOutlet weak var chooseImageButton: UIButton!
    @IBOutlet weak var startButton: UIButton!
    
    func pointFromIndex(index: Int) -> CGPoint
    {
        var point: CGPoint
        var col_pos: Int
        var row_pos: Int
        col_pos = index % kNumberOfColumns
        row_pos = index / kNumberOfColumns
        point = CGPointMake(CGFloat(col_pos), CGFloat(row_pos))
        return point
    }
    
    func indexFromPoint(point: CGPoint) -> Int
    {
        var index = Int(point.y * CGFloat(kNumberOfColumns) + point.x)
        return index
    }
    
    func pieceFrameAtIndex(index: Int) -> CGRect
    {
        var point: CGPoint = self.pointFromIndex(index)
        var width: CGFloat = CGFloat(self.mainView.frame.size.width) / CGFloat(kNumberOfColumns)
        var height: CGFloat = CGFloat(self.mainView.frame.size.height) / CGFloat(kNumberOfRows)
        return CGRectMake(point.x * width, point.y * height, width, height);
    }
    
    func canMovePieceFromPoint(point: CGPoint) -> Bool
    {
        var canMove: Bool
        
        if (CGPointEqualToPoint(self.pointOfBlank!, point)) {
            canMove = false
        } else {
            canMove = self.pointOfBlank!.x == point.x || self.pointOfBlank!.y == point.y
        }
        return canMove
    }
    
    func movePieceFromPointWithAnimation(point: CGPoint, animation: Bool)
    {
        if (!canMovePieceFromPoint(point)) {
            return
        }
        
        //移動方向を決定する
        var step: Int
        if (self.pointOfBlank!.x == point.x) {
            step = self.pointOfBlank!.y > point.y ? kNumberOfColumns : -kNumberOfColumns
        } else {
            step = self.pointOfBlank!.x > point.x ? 1 : -1
        }
        
        //移動対象のピースを格納する配列
        var targetPieceViews: [UIImageView] = []
        
        var indexOfBlank = self.indexFromPoint(self.pointOfBlank!)
        var index = self.indexFromPoint(point)
        
        //移動対象のピースを抽出する
        while index != indexOfBlank {
            for pieceView in self.pieceViews! {
                if pieceView.tag == index {
                    targetPieceViews.append(pieceView)
                    break
                }
            }
            index += step
        }
        
        //移動対象のピースを実際に動かす
        //アニメーションが必要なときは0.2秒かけてアニメーションさせる
        //アニメーションが不要な場合はアニメーション時間を0秒にすることで即座に反映させる
        var duration = animation ? 0.2 : 0
        UIView.animateWithDuration(duration, animations: {() -> Void in
            //このブロック内でアニメーション対象のプロパティを変更すると
            //指定した時間でアニメーションする
            for pieceView in targetPieceViews {
                pieceView.tag += step
                pieceView.frame = self.pieceFrameAtIndex(pieceView.tag)
            }
        })
        
        self.pointOfBlank  = point;
    }
    
    override func viewDidLoad()
    {
        super.viewDidLoad()
        println("\(self.kNumberOfColumns)")
        // Do any additional setup after loading the view, typically from a nib.
    }

    override func didReceiveMemoryWarning()
    {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}

